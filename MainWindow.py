'''
Author: cy 2449471714@qq.com
Date: 2024-03-11 15:01:45
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-21 14:46:26
FilePath: \MagicStickTool\MainWindow.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

'''
魔棒工具窗口主页面
'''
from scripts.utils import getFileBaseName
from PySide6.QtCore import Qt,QStringListModel,QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget,QFileDialog,QMessageBox,QGraphicsScene,QButtonGroup,QCheckBox,QGraphicsLineItem,QGraphicsEllipseItem,QGraphicsPolygonItem
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem,QPixmap,QPainter,QColor
from MainWindowUi import Ui_MainWindow
from CustomGraphicsScene import CustomGraphicsScene
from SegmentationModel import SegmmentationModel
import torch
import os
import multiprocessing 
from LoadingModelDialog import LoadingModelDialog
import cv2
from MaskItem import MaskItem
from CheckBoxComboBox import CheckBoxComboBox
from PySide6.QtTest import QTest
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #set window size
        self.resize(1200,600)
        
        #open image foler click event
        self.ui.actionopen_images_folder.triggered.connect(self.open_image_folder)
        self.ui.actionopen_label_folder.triggered.connect(self.open_label_folder)
        
        #model change event
        self.ui.actionvit_h.triggered.connect(self.changeModel_h)
        self.ui.actionvit_l.triggered.connect(self.changeModel_l)
        self.ui.actionvit_b.triggered.connect(self.changeModel_b)
        
        #warning messagebox
        self.msg_box = QMessageBox(self)
        self.msg_box.setIcon(QMessageBox.Warning)
        self.msg_box.setWindowTitle("警告")
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        
        #set model for list view
        self.image_list_model = QStandardItemModel()
        self.ui.listView.setModel(self.image_list_model)
        
        #set model for label list view
        self.label_list_model = QStandardItemModel()
        self.ui.listView_2.setModel(self.label_list_model)
        
        #bind click event for list view
        self.ui.listView.clicked.connect(self.list_view_clicked)
        
        #set scene for graphics view
        self.image_scene = CustomGraphicsScene()
        self.ui.graphicsView.setScene(self.image_scene)
        self.image_scene.setPrompt("")
        
        #get width and height of graphics view
        self.imagecon_width = self.ui.graphicsView.width()
        self.imagecon_height = self.ui.graphicsView.height()
        
        #set disabled for checkbox
        self.setDisabledforCheckedBox(True)
        #set button group
        self.checkGroup = QButtonGroup()
        self.checkGroup.addButton(self.ui.checkBox)
        self.checkGroup.addButton(self.ui.checkBox_2)
        self.checkGroup.addButton(self.ui.checkBox_3)
        self.checkGroup.setExclusive(True)
        
        #set init state 
        self.currentFolder = ""
        self.currentImagePath = ""
        self.currentLabelFolder = ""
        # self.currentRadio = -1
        self.prompt = ""
        
        self.checkGroup.buttonClicked.connect(self.prompt_clicked)
        
        #init model
        self.dialog = LoadingModelDialog()
        # self.dialog.show()
        self.model_type = "vit_b"
        self.device =  torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.loadCurrentModel()
        # self.dialog.accept()
        self.model_load_in = True
        
        #connect prompt update and predict
        self.image_scene.prompt_update.connect(self.predict_sem)
        
        #all mask
        self.mask_items = []
        
        #out_type
        self.out_type = {
            "mask":True
        }
        self.ui.checkBox_4.setChecked(True)
        self.ui.checkBox_4.setDisabled(True)
        self.ui.checkBox_4.stateChanged.connect(self.output_change)
        
        #msg box
        self.info_box = QMessageBox(self)
        self.info_box.setWindowTitle("提示")
        self.info_box.setIcon(QMessageBox.Information)
        self.info_box.setStandardButtons(QMessageBox.Ok)
        
        #set state checkbox state
        self.setDisabledforStateCheckBox(True)
        self.currentImageIndex = -1
        self.finishedIndex = []
        self.stateCheckGroup = QButtonGroup()
        self.stateCheckGroup.addButton(self.ui.checkBox_6)
        self.stateCheckGroup.addButton(self.ui.checkBox_5)
        self.stateCheckGroup.buttonClicked.connect(self.stateChange)
        self.image_scene.updateState("prompt")
        self.ui.checkBox_6.setChecked(True)
        
        #set button click event
        self.ui.pushButton_2.clicked.connect(self.peviousImage)
        #set button click event
        self.ui.pushButton.clicked.connect(self.nextImage)
        self.ui.pushButton_3.clicked.connect(self.saveButton)
        
        #set window icon
        self.setWindowIcon(QIcon("./assets/icons/magic.png"))  # 使用图标文件路径
        
    def loadCurrentModel(self):
        self.model = SegmmentationModel(device=self.device,type=self.model_type)
        self.model.loadModel()
        
    def open_image_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(None, "选择文件夹", options=options)
        if folder_path:
            image_list = self.get_image_files(folder_path)
            #no image in folder
            if(len(image_list) == 0):
                self.msg_box.setText("未检测到图片(.jpg,.jpeg,.png)文件,请确认是否选择了正确的文件夹！")
                self.msg_box.exec()
            else:
                self.currentFolder = folder_path
                image_basename_list = [getFileBaseName(x) for x in image_list]
                self.image_basename_list = image_basename_list
                #update list view
                self.updateImageList(image_basename_list)
        else:
            self.msg_box.setText("未选择文件夹！")
            self.msg_box.exec()
    
    #get images in folder return list
    def get_image_files(self,folder_path):
        image_extensions = ['.jpg', '.jpeg', '.png']  #just that 
        image_files = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in image_extensions:
                    image_files.append(os.path.join(root, file))

        return image_files
    
    # update list view
    def updateImageList(self,imageList):
        self.image_list_model.clear()
        for item_text in imageList:
            item = QStandardItem(item_text)
            item.setIcon(QIcon("./assets/icons/origin.png"))  # set icon
            self.image_list_model.appendRow(item)
            
    def updateLabelList(self,labelList):
        self.label_list_model.clear()
        for item_text in labelList:
            item = QStandardItem(item_text)
            self.label_list_model.appendRow(item)
        
    def list_view_clicked(self,index):
        self.currentImageIndex = index
        item_value = self.image_list_model.data(index, Qt.DisplayRole)
        #clear paint
        self.clearAllMask()
        self.clearAllPrompt()
        
        #show image in center widget
        self.currentImagePath = self.currentFolder + "/" + item_value
        self.updateImageInCenterWidget(self.currentImagePath)
        
        #update icon 
        self.setListIcon()
        item = self.image_list_model.itemFromIndex(index)
        item.setIcon(QIcon("./assets/icons/ing.png"))
        
        #set prompt abled
        self.setDisabledforCheckedBox(False)
        
        #set atste abled
        self.setDisabledforStateCheckBox(False)
        
        #set default prompt
        self.ui.checkBox.setChecked(True)
        self.prompt = "positive"
        self.image_scene.setPrompt(self.prompt)
        
        #update model image
        self.setModelImage(self.currentImagePath)
        
        #add mask 
        self.addLabelMask()
            
    def updateImageInCenterWidget(self,image_path):
       # load image
        pixmap = QPixmap(image_path)
        pixmap_item = self.image_scene.addPixmap(pixmap)
        pixmap_item.setPos(0, 0)
        
        self.image_scene.image_width = pixmap_item.boundingRect().width()
        self.image_scene.image_hieght = pixmap_item.boundingRect().height()
        
        #scale image to adapt window
        # image_width = pixmap.width()
        # image_height = pixmap.height()
        # scale_radio = min(self.imagecon_width / image_width, self.imagecon_height / image_height)
        # self.currentRadio = scale_radio
        # pixmap_item.setScale(scale_radio)
        
        self.image_scene.image_item = pixmap_item
        
    def setDisabledforCheckedBox(self,checked):
        self.ui.checkBox.setDisabled(checked)
        self.ui.checkBox_2.setDisabled(checked)
        self.ui.checkBox_3.setDisabled(checked)
    def setDisabledforStateCheckBox(self,checked):
        self.ui.checkBox_5.setDisabled(checked)
        self.ui.checkBox_6.setDisabled(checked)
    #open label folder
    def open_label_folder(self):
        if self.currentFolder:
            options = QFileDialog.Options()
            options |= QFileDialog.ShowDirsOnly
            folder_path = QFileDialog.getExistingDirectory(None, "选择文件夹", options=options)
            if folder_path:
                self.currentLabelFolder = folder_path

                #finishedIndex
                files = os.listdir(self.currentLabelFolder)
                self.currentLabelList = [getFileBaseName(file) for file in files]
                
                #set label list
                self.updateLabelList(self.currentLabelList)
                
                label_base_list = [label.split('.')[0] for label in self.currentLabelList]
                
                for index,image_base in enumerate(self.image_basename_list):
                    file_name, file_extension = os.path.splitext(image_base)
                    #image has label?
                    if file_name in label_base_list:
                        item_index = self.image_list_model.index(index, 0)
                        self.finishedIndex.append(item_index)
                        self.setListIcon()
                
            else:
                self.msg_box.setText("未选择文件夹！")
                self.msg_box.exec()
            
        else:
            self.msg_box.setText("请先选择图片文件夹！")
            self.msg_box.exec()
    def prompt_clicked(self,button):
        if button.isChecked():
            self.prompt = button.text()
            self.image_scene.setPrompt(self.prompt)
    
    def changeModel_h(self):
        if self.model_type == "vit_h":
            return
        else:
            self.model_load_in = False
            # self.dialog.show()
            self.model_type = "vit_h"
            self.loadCurrentModel()
            # self.dialog.accept()
            self.model_load_in = True            
            self.msg_box.setText("模型加载成功！")
            self.msg_box.show()
            
    def changeModel_l(self):
        if self.model_type == "vit_l":
            return
        else:
            self.model_load_in = False
            # self.dialog.show()
            self.model_type = "vit_l"
            self.loadCurrentModel()
            # self.dialog.accept()
            self.model_load_in = True
            self.msg_box.setText("模型加载成功！")
            self.msg_box.show()
            
    def changeModel_b(self):
        if self.model_type == "vit_b":
            return
        else:
            self.model_load_in = False
            # self.dialog.show()
            self.model_type = "vit_b"
            self.loadCurrentModel()
            # self.dialog.accept()
            self.model_load_in = True
            self.msg_box.show()
    #set model using image
    def setModelImage(self,image_path):
        self.model.setCurrentImage(imagePath=image_path)
        
    #model predict
    def predict_sem(self,positive_points,negatives_points,boxes):
        # self.clearPointLineAndPolygon()
        self.clearAllMask()
        split_masks = self.model.predict(positive_points,negatives_points,boxes)
        self.generateMaskItems(split_masks)
        
        #set out type
        self.ui.checkBox_4.setDisabled(False)
        
    #generateMaskItem
    def generateMaskItems(self,split_masks):
        for i,mask in enumerate(split_masks):
            new_mask = MaskItem(mask,self.image_scene,i)
            new_mask.delete_item.connect(self.deleteMaskItem)
            #set mask_item state
            new_mask.setState(self.image_scene.state)
            self.mask_items.append(new_mask)
    def clearPointLineAndPolygon(self):
        for mask_item in self.mask_items:
            mask_item.clear()
        self.mask_items.clear()
        # for item in self.image_scene.items():
        #     if isinstance(item, QGraphicsLineItem) or isinstance(item, QGraphicsEllipseItem) or isinstance(item, QGraphicsPolygonItem):
        #         self.image_scene.removeItem(item)
    def deleteMaskItem(self,index):
        self.mask_items[index] = None
    def output_change(self,state):
        if state == 2:
            self.out_type["mask"] = True
        elif state == 0:
            self.out_type["mask"] = False
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_S:
            if self.currentImagePath == "":
                return
            #judge label path
            if self.currentLabelFolder == "":
                self.msg_box.setText("未选择标签文件输出文件夹！")
                self.msg_box.exec()
                return
            #judge has mask?
            mask_num = self.judgeMaskNumm()
            if mask_num == 0:
                self.msg_box.setText("暂无需要保存的mask！")
                self.msg_box.exec()
                return

            #save mask in labelPath
            self.saveMasks()
        else:
            super().keyPressEvent(event)
    #judge mask num
    def judgeMaskNumm(self):
        num = 0
        for maskItem in self.mask_items:
            if maskItem is not None:
                num+=1
        return num
    #save all mask
    def saveMasks(self):
        image_height = self.model.currentImage.shape[0]
        image_width = self.model.currentImage.shape[1]
        if self.out_type["mask"]:
            output_image = np.zeros((image_height,image_width))
            for maskItem in self.mask_items:
                if maskItem is not None:
                    origin_mask = maskItem.origin_mask
                    output_image[origin_mask != 0] = 255
            output_image = np.repeat(output_image[...,np.newaxis],repeats=3,axis=-1).astype(np.uint8)
            
            imageName = os.path.splitext(os.path.basename(self.currentImagePath))[0]
            #save image in folder
            cv2.imwrite(self.currentLabelFolder + "/" + imageName + ".png",output_image)
            
            #info box
            self.info_box.setText("保存成功！")
            self.info_box.show()
            
            #set icon
            if self.currentImageIndex not in self.finishedIndex:
                self.finishedIndex.append(self.currentImageIndex)
                self.setListIcon()
            
            #update label list
            self.appendLabelList(imageName + ".png")
            
    def setListIcon(self):
        for row in range(self.image_list_model.rowCount()):
            item = self.image_list_model.item(row)
            item.setIcon(QIcon("./assets/icons/origin.png"))
            
            for index in self.finishedIndex:
                item = self.image_list_model.itemFromIndex(index)
                item.setIcon(QIcon("./assets/icons/fineshed.png"))
    def appendLabelList(self,label):        
        if self.label_list_model.findItems(label):
            return
        else:
            item = QStandardItem(label)
            self.label_list_model.appendRow(item)
    def stateChange(self,button):
        if button.isChecked():
            state = button.text()
            if state == "微调":
                self.image_scene.updateState("adapt")
                for mi in self.mask_items:
                    mi.setState("adapt")
            elif state == "标注":
                self.image_scene.updateState("prompt")
                for mi in self.mask_items:
                    if mi is not None:
                        mi.setState("prompt")
    def clearAllMask(self):
        for mi in self.mask_items:
            if mi is not None:
                mi.clear()
        self.mask_items.clear()
    def clearAllPrompt(self):
        self.image_scene.clear()
    def addLabelMask(self):
        filename_with_extension = os.path.basename(self.currentImagePath)
        image_base = os.path.splitext(filename_with_extension)[0]
        if self.currentLabelFolder:
            label_base_list = [label.split('.')[0] for label in self.currentLabelList]
            try:
                index = label_base_list.index(image_base)
                mask_path = self.currentLabelFolder + "/" + self.currentLabelList[index]
                #add mask 2 image
                image_mask = cv2.imread(mask_path)[:,:,0]
                split_masks = self.model.splitMask(image_mask)
                self.generateMaskItems(split_masks)
            except ValueError:
                pass
    def changeImage(self,index):
        index_to_click = index
        model_index = self.image_list_model.index(index_to_click, 0)
        rect = self.ui.listView.visualRect(model_index)
        center = rect.center()
        QTest.mouseClick(self.ui.listView.viewport(), Qt.LeftButton, Qt.NoModifier, center)
    #get the previous image index
    def peviousImage(self):
        if self.currentImageIndex == -1:
            return
        else:
            index = self.currentImageIndex.row()
            if index == 0:
                return
            else:
                self.changeImage(index-1)
    def nextImage(self):
        if self.currentImageIndex == -1:
            return
        else:
            index = self.currentImageIndex.row()
            if index == len(self.image_basename_list) - 1:
                return
            else:
                self.changeImage(index + 1)
    def saveButton(self):
        if self.currentImagePath == "":
            return
        #judge label path
        if self.currentLabelFolder == "":
            self.msg_box.setText("未选择标签文件输出文件夹！")
            self.msg_box.exec()
            return
        #judge has mask?
        mask_num = self.judgeMaskNumm()
        if mask_num == 0:
            self.msg_box.setText("暂无需要保存的mask！")
            self.msg_box.exec()
            return
        self.saveMasks()
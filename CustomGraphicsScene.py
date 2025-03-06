'''
Author: cy 2449471714@qq.com
Date: 2024-03-12 15:41:18
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-20 11:52:37
FilePath: \MagicStickTool\CustomGraphicsScene.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import Qt,QRectF,Signal
from PySide6.QtGui import QPainter, QPen, QColor,QBrush
class CustomGraphicsScene(QGraphicsScene):
    prompt_update = Signal(list,list,list)
    def __init__(self):
        super().__init__()
        self.image_item = None
        
        self.positive_points = []
        self.negatives_points = []
        self.boxes = []
        
        self.currentBoxStartPoint = None
        self.currentBoxEndPoint = None
        self.current_rect_item = None
        
        self.state = "prompt"
    #mouse press event
    def mousePressEvent(self, event):
        if self.prompt and self.state == "prompt":
            if event.button() == Qt.LeftButton:
                pos = event.scenePos()
                #in picture bbox?
                if self.image_item is not None and self.image_item.contains(pos):
                    if self.prompt == "positive":
                        self.positive_points.append([pos.x(),pos.y()])
                        self.paintPoint(pos)
                        self.prompt_update.emit(self.positive_points,self.negatives_points,self.boxes)
                    elif self.prompt == "negative":
                        self.negatives_points.append([pos.x(),pos.y()]) 
                        self.prompt_update.emit(self.positive_points,self.negatives_points,self.boxes)
                        self.paintPoint(pos)
                    elif self.prompt == "box":
                        self.currentBoxStartPoint = pos
        super().mousePressEvent(event)
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.currentBoxStartPoint is not None and self.prompt == "box" and self.state == "prompt":  
            if  self.current_rect_item is None: 
                self.current_rect_item = self.addRect(0, 0, 0, 0)
                self.current_rect_item.setPen(QPen(Qt.blue))
                brush_color = QColor(Qt.blue) 
                brush_color.setAlpha(0)  
                self.current_rect_item.setBrush(QBrush(brush_color))
                
            # 更新矩形的位置和大小
            rect = QRectF(self.currentBoxStartPoint, event.scenePos()).normalized()
            self.current_rect_item.setRect(rect)
        super().mouseMoveEvent(event)
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.prompt == "box" and self.state == "prompt":
            self.currentBoxEndPoint = event.scenePos()
            
            box_left_x = min(self.currentBoxStartPoint.x(), self.currentBoxEndPoint.x())
            box_left_y = min(self.currentBoxStartPoint.y(), self.currentBoxEndPoint.y())
            box_width = abs(self.currentBoxStartPoint.x() - self.currentBoxEndPoint.x())
            box_height = abs(self.currentBoxStartPoint.y() - self.currentBoxEndPoint.y())
            self.boxes.append([box_left_x,box_left_y,box_left_x + box_width,box_left_y + box_height])
            
            self.currentBoxStartPoint = None
            self.currentBoxEndPoint = None
            self.current_rect_item = None
            
            self.prompt_update.emit(self.positive_points,self.negatives_points,self.boxes)
        super().mouseReleaseEvent(event)
       

    def setPrompt(self,prompt):
        self.prompt = prompt
    def clearPrompt(self):
        self.positive_points.clear()
        self.negatives_points.clear()
        self.boxes.clear()
    def paintPoint(self,pos):
        if self.prompt == "positive":
            point_item = self.addEllipse(pos.x() - 4, pos.y() - 4, 8, 8, QPen(Qt.blue), QColor(Qt.blue))
        elif self.prompt == "negative":
            point_item = self.addEllipse(pos.x() - 4, pos.y() - 4, 8, 8, QPen(Qt.red), QColor(Qt.red))
    def updateState(self,state):
        self.state = state
    
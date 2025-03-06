'''
Author: cy 2449471714@qq.com
Date: 2024-03-14 15:06:45
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-21 14:52:06
FilePath: \MagicStickTool\MaskItem.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
一个MaskItem代表独立的一块mask，可以编辑其顶点位置，或者删除整个图形
'''
from HoverablePolygonItem import HoverablePolygonItem,HoverablePolygonItemWrapper
from DraggableEllipseItem import DraggableEllipseItem,DraggableEllipseItemWrapper
from PySide6.QtGui import QPolygonF, QPen, QColor,QBrush
import cv2
from PySide6.QtCore import Qt,QPointF,QObject,Signal
from scripts.utils import remove_redundant_points

class MaskItem(QObject):
    delete_item = Signal(int)
    def __init__(self,mask,image_scene,index):
        super().__init__()
        self.point_items = []
        self.line_items = []
        self.polygon_item = []
        self.index = index
        self.image_scene = image_scene
        self.origin_mask = mask
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = contours[0]
        polygon = QPolygonF()
        
        sample_points = [p[0] for p in contour]
        sample_points = remove_redundant_points(sample_points,threshold=10)
        # print(sample_points)
        for i,point in enumerate(sample_points):
            x, y = point[0],point[1]
            polygon.append(QPointF(x,y))
            
            #paint point
            point_item = DraggableEllipseItem(x - 3, y - 3, 6, 6)
            point_item.setZValue(10)
            point_item.saveOriginPos(x,y)
            point_item.setIndex(i)
            image_scene.addItem(point_item)
            
            point_item_wapper = DraggableEllipseItemWrapper(point_item)
            point_item_wapper.updatePos.connect(self.update_point_pos)
            # image_scene.addEllipse(x - 2, y - 2, 4, 4, QPen(Qt.yellow), QColor(Qt.yellow))
            self.point_items.append(point_item)
            #paint line
            if i != (len(sample_points) - 1):
                next_point = sample_points[i+1]
                x_next = next_point[0]
                y_next = next_point[1]
                line_item = image_scene.addLine(x, y, x_next, y_next)
                line_item.start_index = i
                line_item.end_index = i + 1
                
                self.line_items.append(line_item)
        #paint polygon
        hover_polygon_item = HoverablePolygonItem(polygon)
        image_scene.addItem(hover_polygon_item)
        self.polygon_item.append(hover_polygon_item)
        
        wrapper = HoverablePolygonItemWrapper(hover_polygon_item)
        wrapper.delete_mask.connect(self.clear)
        
    def clear(self):
        #clear all item
        for point_item in self.point_items:
            self.image_scene.removeItem(point_item)
        for line_item in self.line_items:
            self.image_scene.removeItem(line_item)
        for polygon_item in self.polygon_item:
            self.image_scene.removeItem(polygon_item)
        self.delete_item.emit(self.index)
    
    def update_point_pos(self,index,pos):
        # print(pos.x(),pos.y())
        #update line 
        for i in range(len(self.line_items)):
            if self.line_items[i].start_index == index:
                end_point = self.line_items[i].line().p2()
                self.line_items[i].setLine(pos.x(),pos.y(),end_point.x(),end_point.y())
            elif self.line_items[i].end_index == index:
                start_point = self.line_items[i].line().p1()
                self.line_items[i].setLine(start_point.x(),start_point.y(),pos.x(),pos.y())
        #update polygonitem
        polygonItem =self.polygon_item[0]
        vertices = polygonItem.polygon().toList()
        vertices[index] = QPointF(pos.x(), pos.y())
        newPolygon = QPolygonF(vertices)
        polygonItem.setPolygon(newPolygon)
    def setState(self,state):
        # print(state)
        for pi in self.point_items:
            pi.setCurrentState(state)
        self.state = state
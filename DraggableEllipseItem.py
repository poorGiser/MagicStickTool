'''
Author: cy 2449471714@qq.com
Date: 2024-03-20 11:28:52
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-21 12:03:11
FilePath: \代码\MagicStickTool\DraggableEllipseItem.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import sys
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PySide6.QtCore import Qt,Signal,QObject,QPointF
from PySide6.QtGui import QColor
class DraggableEllipseItem(QGraphicsEllipseItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsGeometryChanges)
        # set color 
        self.setBrush(QColor(0, 0, 0)) 
        self.setPen(QColor(255, 255, 0)) 
    
    #set index for point
    def setIndex(self,index):
        self.index = index
    def saveOriginPos(self,x,y):
        self.origin_x = x
        self.origin_y = y
    def setCurrentState(self,state):
        self.state = state
        
class DraggableEllipseItemWrapper(QObject):
    updatePos = Signal(int,QPointF)
    def __init__(self, point_item):
        super().__init__()
        self.point_item = point_item
        self.point_item.itemChange = self.itemChange

    def itemChange(self, change, value):
        if change == QGraphicsEllipseItem.ItemPositionChange and self.point_item.scene() and self.point_item.state == "adapt":
            # print(self.point_item.origin_x)
            # print(self.point_item.origin_y)
            
            # Restrict the movement within the scene bounds
            if self.point_item.origin_x + value.x() > 256 or self.point_item.origin_x + value.x() < 0:
                return
            if self.point_item.origin_y + value.y() > 256 or self.point_item.origin_y + value.y() < 0:
                return
            
            new_pos = QPointF()
            new_pos.setX(self.point_item.origin_x + value.x())
            new_pos.setY(self.point_item.origin_y + value.y())  
            # new_pos.setX(min(max(new_pos.x(), 0), 256))
            # new_pos.setY(min(max(new_pos.y(), 0), 256))
            
            self.updatePos.emit(self.point_item.index,new_pos)
            return value
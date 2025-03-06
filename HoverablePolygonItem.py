from PySide6.QtWidgets import QGraphicsPolygonItem, QGraphicsScene, QApplication, QMainWindow
from PySide6.QtCore import Qt,Signal,QObject
from PySide6.QtGui import QPolygonF, QColor, QPen, QBrush

class HoverablePolygonItem(QGraphicsPolygonItem):
    def __init__(self, polygon, parent=None):
        super().__init__(parent)
        self.setPolygon(polygon)
        defaultColor = QColor(Qt.green)
        defaultColor.setAlpha(128)
        self.setBrush(QBrush(defaultColor))
        self.setAcceptHoverEvents(True)  
        self.hoverStatus = False
    def hoverEnterEvent(self, event):
        color = QColor(Qt.red)
        color.setAlpha(64)
        self.setBrush(QBrush(color))
        self.hoverStatus = True
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        color = QColor(Qt.green)
        color.setAlpha(128)
        self.setBrush(QBrush(color))
        self.hoverStatus = False
        
        super().hoverLeaveEvent(event)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
           self.delete_mask.emit()
        super().mousePressEvent(event)
        
class HoverablePolygonItemWrapper(QObject):
    delete_mask = Signal()
    def __init__(self, polygon_item):
        super().__init__()
        self.polygon_item = polygon_item
        self.polygon_item.mousePressEvent = self.mousePressEvent

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.delete_mask.emit()
        
    
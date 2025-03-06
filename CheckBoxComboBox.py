'''
Author: cy 2449471714@qq.com
Date: 2024-03-15 10:12:18
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-15 10:12:25
FilePath: \MagicStickTool\CheckBoxComboBox.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PySide6.QtWidgets import QApplication, QComboBox, QCheckBox

class CheckBoxComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view().pressed.connect(self.handle_item_pressed)

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if isinstance(item, QCheckBox):
            item.setCheckState(not item.checkState())
            self.currentIndexChanged.emit(self.currentIndex())  # Emit currentIndexChanged signal

    def addItem(self, item, checkable=False):
        if checkable:
            checkbox = QCheckBox()
            checkbox.setText(item)
            super().addItem(item, checkbox)
        else:
            super().addItem(item)

    def checkedItems(self):
        checked_items = []
        for i in range(self.count()):
            item = self.itemData(i)
            if isinstance(item, QCheckBox) and item.isChecked():
                checked_items.append(self.itemText(i))
        return checked_items



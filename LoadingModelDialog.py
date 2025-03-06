import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from ui.Loading import Ui_Dialog

class LoadingModelDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
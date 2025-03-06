'''
Author: cy 2449471714@qq.com
Date: 2024-03-11 15:00:25
LastEditors: cy 2449471714@qq.com
LastEditTime: 2024-03-11 15:13:28
FilePath: \MagicStickTool\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    window.show()
    
    sys.exit(app.exec())

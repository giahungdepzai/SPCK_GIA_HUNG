from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class HomePage(QMainWindow): 
    def __init__(self): 
        super().__init__()
        uic.loadUi("./gui/main.ui", self) 

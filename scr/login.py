import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor
from qtwidgets import AnimatedToggle
from PyQt6 import uic

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./gui/dang_nhap.ui", self)
        
        self.btn_register.clicked.connect(self.OpenRegisterForm)
        self.btnLogin.clicked.connect(self.Login)
        self.registerWindow = None
        self.homePageWindow = None
        
        self.chuxShowPassword.stateChanged.connect(self.show_password)

    def OpenRegisterForm(self):
        from register import Register
        if self.registerWindow == None:
            self.registerWindow = Register()
        
        self.registerWindow.show()
        self.hide()

    def Login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        if email == 'Admin' and password == 'Admin':
            if self.homePageWindow == None:
                from homepage import HomePage
                self.homePageWindow = HomePage()
            
            self.homePageWindow.show()
            self.hide()

    def show_password(self):
        if self.chuxShowPassword.isChecked():
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/DO MANH HUNG/Documents/Zalo Received Files/New folder/gui.ui", self)

        # Tạo toggle switch
        toggle = AnimatedToggle(checked_color="#7F1DFF", pulse_checked_color="#F5F5FF")

        # Gắn toggle vào frame đã tạo trong Qt Designer (đảm bảo self.frame là QFrame)
        layout = QVBoxLayout()
        layout.addWidget(toggle)

        # Gắn layout cho frame
        self.frame.setLayout(layout)

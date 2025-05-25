import sys
import json
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
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
    email = self.txtEmail.text().strip()
    password = self.txtPassword.text().strip()

    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        QMessageBox.critical(self, "Lỗi", "Không tìm thấy file users.json")
        return

    for user in users:
        if user["email"] == email and user["password"] == password:
            # Nếu đúng, mở trang chủ
            if self.homePageWindow is None:
                from homepage import HomePage
                self.homePageWindow = HomePage()

            self.homePageWindow.show()
            self.hide()
            return

    # Nếu không khớp
    QMessageBox.warning(self, "Đăng nhập thất bại", "Email hoặc mật khẩu không đúng.")

    def show_password(self):
        if self.chuxShowPassword.isChecked():
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

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

    def xu_ly_dang_nhap(self):
        """Xử lý đăng nhập bằng cách kiểm tra thông tin tài khoản"""
        username = self.txtUsername.text()
        password = self.txtpass.text()

        try:
            # Đọc file JSON chứa danh sách tài khoản
            with open("code/account.json", "r") as file:
                data = json.load(file)

            # Duyệt qua tất cả các tài khoản trong danh sách
            for account in data["accounts"]:
                if account["username"] == username and account["password"] == password:
                    # Nếu thông tin đúng, lưu tài khoản hiện tại vào file current_account.json
                    with open("code/current_account.json", "w") as file:
                        json.dump({"current_account": username}, file, indent=4)

                    # Mở cửa sổ Home
                    from homepage import Home
                    self.homewindow = Home()
                    self.homewindow.show()
                    self.close()
                    return

            # Nếu không tìm thấy tài khoản phù hợp
            QMessageBox.critical(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
        except FileNotFoundError:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy file account.json")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Lỗi", "File account.json bị lỗi định dạng")

    def show_password(self):
        if self.chuxShowPassword.isChecked():
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

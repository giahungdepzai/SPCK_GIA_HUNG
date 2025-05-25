import json
from PyQt6.QtWidgets import QMainWindow, QLineEdit
from PyQt6 import uic 

class Register(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        uic.loadUi("./gui/register.ui", self) 
        self.btnReturn.clicked.connect(self.OpenLoginForm)
        self.btnLogin.clicked.connect(self.OpenLoginForm)
        self.loginWindow = None
    
    def xu_ly_dang_ky(self):
        txtUsername = self.txtUsername.text().strip()
        txtpass = self.txtpass.text().strip()
        txtRepass = self.txtRepass.text().strip()
        
        if txtUsername == "" or txtpass == "" or txtRepass == "":
            self.thongBao("Thông báo", "Vui lòng nhập đầy đủ thông tin")
            return
        
        if txtpass != txtRepass:
            self.thongBao("Thông báo", "Mật khẩu không trùng khớp")
            return
        
        with open("code/account.json", "r") as file:
            data = json.load(file)
            
        for item in data["accounts"]:
            if item["username"] == txtUsername:
                self.thongBao("Thông báo", "Tài khoản đã tồn tại")
                return
            
        data["accounts"].append(dict(username = txtUsername, password = txtpass,balance = 0))
        with open("code/account.json", "w") as file:
            json.dump(data, file, indent=4)
            self.thongBao("Thông báo", "Đăng ký tài khoản thành công")
        self.Home()


        
    def OpenLoginForm(self):
        from login import Login
        
        if self.loginWindow == None:
            self.loginWindow = Login()
            
        self.loginWindow.show()
        
        self.hide()
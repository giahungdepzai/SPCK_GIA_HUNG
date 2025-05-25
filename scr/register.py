from PyQt6.QtWidgets import QMainWindow, QLineEdit
from PyQt6 import uic 

class Register(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        uic.loadUi("./gui/register.ui", self) 
        self.btnReturn.clicked.connect(self.OpenLoginForm)
        self.btnLogin.clicked.connect(self.OpenLoginForm)
        self.loginWindow = None
    
    def Login(self):
        fullname = self.txtfullname.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        if email == 'Admin' and password == 'Admin' and fullname == 'Admin':
            if self.loginWindow == None:
                from login import Login
                self.loginWindow = Login()
            
            self.loginWindow.show()
            self.hide()

        
    def OpenLoginForm(self):
        from login import Login
        
        if self.loginWindow == None:
            self.loginWindow = Login()
            
        self.loginWindow.show()
        
        self.hide()
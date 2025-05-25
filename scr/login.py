from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dark_mode = False
        self.ui.btnToggleTheme.clicked.connect(self.toggle_theme)

    def toggle_theme(self):
        if not self.dark_mode:
            # Chuyển sang dark mode
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
            dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
            dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
            dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))

            QApplication.setStyle("Fusion")
            QApplication.setPalette(dark_palette)
            self.dark_mode = True
        else:
            # Quay lại light mode mặc định
            QApplication.setPalette(QApplication.style().standardPalette())
            self.dark_mode = False

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
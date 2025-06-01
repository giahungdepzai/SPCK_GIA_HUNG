from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thêm món ăn")
        self.layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.layout.addWidget(QLabel("Tên món ăn:"))
        self.layout.addWidget(self.title_input)

        self.btn_ok = QPushButton("Thêm")
        self.btn_ok.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_ok)

        self.setLayout(self.layout)

    def return_input_fields(self):
        return {"title": self.title_input.text()}


class EditDialog(QDialog):
    def __init__(self, item_data):
        super().__init__()
        self.setWindowTitle("Sửa món ăn")
        self.layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setText(item_data.get("title", ""))
        self.layout.addWidget(QLabel("Tên món ăn mới:"))
        self.layout.addWidget(self.title_input)

        self.btn_ok = QPushButton("Lưu")
        self.btn_ok.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_ok)

        self.setLayout(self.layout)

    def return_input_fields(self):
        return {"title": self.title_input.text()}
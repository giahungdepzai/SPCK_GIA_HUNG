from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSpinBox
from PyQt6.QtCore import Qt

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thêm món ăn mới")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title input
        title_layout = QHBoxLayout()
        title_label = QLabel("Tên món:")
        self.title_input = QLineEdit()
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_input)
        layout.addLayout(title_layout)

        # Price input
        price_layout = QHBoxLayout()
        price_label = QLabel("Giá:")
        self.price_input = QLineEdit()
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_input)
        layout.addLayout(price_layout)

        # Quantity input
        quantity_layout = QHBoxLayout()
        quantity_label = QLabel("Số lượng:")
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(0)
        self.quantity_input.setMaximum(999)
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(self.quantity_input)
        layout.addLayout(quantity_layout)

        # Description input
        desc_layout = QHBoxLayout()
        desc_label = QLabel("Mô tả:")
        self.desc_input = QLineEdit()
        desc_layout.addWidget(desc_label)
        desc_layout.addWidget(self.desc_input)
        layout.addLayout(desc_layout)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Lưu")
        cancel_button = QPushButton("Hủy")
        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def return_input_fields(self):
        return {
            "title": self.title_input.text(),
            "price": self.price_input.text(),
            "quantity": self.quantity_input.value(),
            "description": self.desc_input.text()
        }

class EditDialog(QDialog):
    def __init__(self, food_item):
        super().__init__()
        self.food_item = food_item
        self.setWindowTitle("Sửa món ăn")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title input
        title_layout = QHBoxLayout()
        title_label = QLabel("Tên món:")
        self.title_input = QLineEdit(self.food_item.get('title', ''))
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_input)
        layout.addLayout(title_layout)

        # Price input
        price_layout = QHBoxLayout()
        price_label = QLabel("Giá:")
        self.price_input = QLineEdit(str(self.food_item.get('price', '')))
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_input)
        layout.addLayout(price_layout)

        # Quantity input
        quantity_layout = QHBoxLayout()
        quantity_label = QLabel("Số lượng:")
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(0)
        self.quantity_input.setMaximum(999)
        self.quantity_input.setValue(self.food_item.get('quantity', 0))
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(self.quantity_input)
        layout.addLayout(quantity_layout)

        # Description input
        desc_layout = QHBoxLayout()
        desc_label = QLabel("Mô tả:")
        self.desc_input = QLineEdit(self.food_item.get('description', ''))
        desc_layout.addWidget(desc_label)
        desc_layout.addWidget(self.desc_input)
        layout.addLayout(desc_layout)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Lưu")
        cancel_button = QPushButton("Hủy")
        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def return_input_fields(self):
        return {
            "title": self.title_input.text(),
            "price": self.price_input.text(),
            "quantity": self.quantity_input.value(),
            "description": self.desc_input.text()
        }
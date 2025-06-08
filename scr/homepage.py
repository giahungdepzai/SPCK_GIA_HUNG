from PyQt6.QtWidgets import QMainWindow, QListWidget, QMessageBox, QDialog, QLineEdit, QLabel
from PyQt6 import uic
from PyQt6.QtCore import Qt
from database import database
from dialogs import AddDialog, EditDialog
from login import Login

class HomePage(QMainWindow): 
    def __init__(self): 
        super().__init__()
        uic.loadUi("./gui/main.ui", self)
        self.food_crud = FoodCRUD(self)
        self.setup_connections()
        self.setup_ui()

    def setup_ui(self):
        self.foodList.addItems(database.food_title_list)
        if self.foodList.count() > 0:
            self.foodList.setCurrentRow(0)

    def setup_connections(self):
        self.btnAdd.mousePressEvent = lambda e: self.food_crud.add()
        self.btnEdit.mousePressEvent = lambda e: self.food_crud.edit()
        self.btnDelete.mousePressEvent = lambda e: self.food_crud.delete()
        self.btnDetail.mousePressEvent = lambda e: self.food_crud.detail()
        self.label_1.mousePressEvent = lambda e: self.logout()
        self.label_9.mousePressEvent = lambda e: self.show_search_results()
        self.label_10.mousePressEvent = lambda e: self.sort_by_price()
        
        self.lineEdit.textChanged.connect(self.food_crud.search)

    def show_search_results(self):
        search_text = self.lineEdit.text().strip()
        if search_text:
            matched_items = database.search_by_title(search_text)
            self.foodList.clear()
            self.foodList.addItems([f"{item['title']} - {item['price']}đ - SL: {item.get('quantity', 0)} - {item.get('description', '')}" for item in matched_items])
        else:
            self.foodList.clear()
            self.foodList.addItems(database.food_title_list)

    def sort_by_price(self):
        sorted_items = database.sort_by_price()
        self.foodList.clear()
        self.foodList.addItems([f"{item['title']} - {item['price']}đ - SL: {item.get('quantity', 0)} - {item.get('description', '')}" for item in sorted_items])

    def logout(self):
        reply = QMessageBox.question(self, 'Đăng xuất', 
                                   'Bạn có chắc muốn đăng xuất?',
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
            self.login_window = Login()
            self.login_window.show()

class FoodCRUD:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window
        self.foodList = self.main_window.findChild(QListWidget, "foodList")
        self.searchInput = self.main_window.findChild(QLineEdit, "lineEdit")

    def add(self):
        add_dialog = AddDialog()
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            database.add_item_from_dict(inputs)
            self.search()  

    def edit(self):
        if not self.foodList or self.foodList.currentRow() < 0:
            return
        item = self.foodList.currentItem()
        if item is None:
            return
        item_title = item.text().split(" - ")[0]  
        edit_item = database.get_item_by_title(item_title)
        if edit_item:
            edit_dialog = EditDialog(edit_item)
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                database.edit_item_from_dict(item_title, inputs)
                self.search()  

    def delete(self):
        if not self.foodList or self.foodList.currentRow() < 0:
            return
        item = self.foodList.currentItem()
        if item is None:
            return
        item_title = item.text().split(" - ")[0]  
        question = QMessageBox.question(self.main_window, "Xóa món ăn",
                                      "Bạn có chắc muốn xóa món này?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            database.delete_item(item_title)
            self.search()  

    def search(self):
        search_text = self.searchInput.text().strip()
        if search_text:
            matched_items = database.search_by_title(search_text)
            self.foodList.clear()
            self.foodList.addItems([f"{item['title']} - {item['price']}đ - SL: {item.get('quantity', 0)} - {item.get('description', '')}" for item in matched_items])
        else:
            self.foodList.clear()
            self.foodList.addItems(database.food_title_list)
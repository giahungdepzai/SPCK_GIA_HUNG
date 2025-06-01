from PyQt6.QtWidgets import QMainWindow, QListWidget, QMessageBox,QDialog
from PyQt6 import uic

# Giả sử bạn đã import hoặc định nghĩa AddDialog, EditDialog và database đúng

class HomePage(QMainWindow): 
    def __init__(self): 
        super().__init__()
        uic.loadUi("./gui/main.ui", self)
        self.food_crud = FoodCRUD(self)

class FoodCRUD:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window
        self.foodList = self.main_window.findChild(QListWidget, "foodList")

    def add(self):
        curr_index = self.foodList.currentRow()
        from dialogs import AddDialog
        add_dialog = AddDialog()
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            self.foodList.insertItem(curr_index, inputs["title"])
            database.add_item_from_dict(inputs)

    def edit(self):
        curr_index = self.foodList.currentRow()
        item = self.foodList.item(curr_index)
        if item is None:
            return
        item_title = item.text()
        edit_item = database.get_item_by_title(item_title)
        edit_dialog = EditDialog(edit_item)
        if edit_dialog.exec():
            inputs = edit_dialog.return_input_fields()
            item.setText(inputs["title"])
            database.edit_item_from_dict(item_title, inputs)

    def delete(self):
        curr_index = self.foodList.currentRow()
        item = self.foodList.item(curr_index)
        if item is None:
            return
        item_title = item.text()
        question = QMessageBox.question(self.main_window, "Xóa món ăn",
                                        "Bạn có chắc muốn xóa món này?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            self.foodList.takeItem(curr_index)
            database.delete_item(item_title)
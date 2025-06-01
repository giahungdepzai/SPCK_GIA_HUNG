from PyQt6.QtWidgets import QMainWindow, QApplication, QListWidget
from PyQt6 import uic

class HomePage(QMainWindow): 
    def __init__(self): 
        super().__init__()
        uic.loadUi("./gui/main.ui", self)
        self.food_crud = FoodCRUD(self)

class FoodCRUD():
    def add(self):
        def __init__(self, main_window: HomePage):
            self.main_window = main_window
            self.foodList = self.main_window.findChild(QListWidget, "foodList")
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            widgets.animeList.insertItem(currIndex, inputs["title"])
            database.add_item_from_dict(inputs)

    def edit(self):
        curr_index = widgets.animeList.currentRow()
        item = widgets.animeList.item(curr_index)
        item_title = item.text()
        edit_item = database.get_item_by_title(item_title)
        if item is not None:
            edit_dialog = EditDialog(edit_item)
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                item.setText(inputs["title"])
                database.edit_item_from_dict(item_title, inputs)

    def delete(self):
        curr_index = widgets.animeList.currentRow()
        item = widgets.animeList.item(curr_index)
        item_title = item.text()
        if item is None:
            return
        question = QMessageBox.question(self, "Remove Anime",
                                        "Do you want to remove this anime?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            item = widgets.animeList.takeItem(curr_index)
            database.delete_item(item_title)

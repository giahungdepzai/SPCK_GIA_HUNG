import json
import os
from datetime import datetime

class FoodDatabase:
    def __init__(self):
        self.data_file = "food_data.json"
        self.food_items = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.food_items = json.load(f)
        else:
            self.food_items = []
            self.save_data()

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.food_items, f, ensure_ascii=False, indent=4)

    def add_item_from_dict(self, item_dict):
        item_dict['id'] = len(self.food_items) + 1
        item_dict['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.food_items.append(item_dict)
        self.save_data()

    def edit_item_from_dict(self, old_title, new_data):
        for item in self.food_items:
            if item['title'] == old_title:
                item.update(new_data)
                break
        self.save_data()

    def delete_item(self, title):
        self.food_items = [item for item in self.food_items if item['title'] != title]
        self.save_data()

    def get_item_by_title(self, title):
        for item in self.food_items:
            if item['title'] == title:
                return item
        return None

    def search_by_title(self, search_text):
        search_text = search_text.lower()
        return [item for item in self.food_items if search_text in item['title'].lower()]

    def sort_by_price(self):
        return sorted(self.food_items, key=lambda x: float(x.get('price', 0)), reverse=True)

    @property
    def food_title_list(self):
        return [f"{item['title']} - {item['price']}đ - SL: {item.get('quantity', 0)} - Mô tả: {item.get('description', '')}" for item in self.food_items]

database = FoodDatabase()

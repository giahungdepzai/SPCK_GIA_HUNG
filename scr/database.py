_food_storage = []

def add_item_from_dict(item):
    _food_storage.append(item)

def get_item_by_title(title):
    for item in _food_storage:
        if item["title"] == title:
            return item
    return {}

def edit_item_from_dict(old_title, new_item):
    for i, item in enumerate(_food_storage):
        if item["title"] == old_title:
            _food_storage[i] = new_item
            break

def delete_item(title):
    global _food_storage
    _food_storage = [item for item in _food_storage if item["title"] != title]

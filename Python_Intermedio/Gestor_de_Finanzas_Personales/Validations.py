import Movements
import data as dt


def category_validation(category_to_validate):
    categories_list = dt.read_categories()
    for categories_in_list in categories_list:
        if category_to_validate in categories_list:
            raise ValueError("Category Already exist")
    return category_to_validate

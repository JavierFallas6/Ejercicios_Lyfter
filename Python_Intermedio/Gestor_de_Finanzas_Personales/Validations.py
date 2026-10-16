import movements as move


def validate_category(category_to_validate):
    categories_list = move.PersonalFinancialManager()
    categories_list = categories_list.categories_record
    categories_list = [category.lower() for category in categories_list]

    if category_to_validate.lower() in categories_list:
        raise ValueError("Category Already exist")
    return category_to_validate

def validate_category_empty(category):
    if not category:
        raise ValueError("Can not add an empty Category, please add Category")
    return category

def validate_amount(amount_to_validate):
    try:
        return float(amount_to_validate)
    except (ValueError, TypeError):
        raise ValueError("Amount must be a number")

def validate_amount_not_less_than_zero(amount_to_validate):
        if amount_to_validate <= 0: 
            raise ValueError("Amount cannot be less or equal to 0")
        return amount_to_validate

def validate_description_empty(description_to_validate):
    if not description_to_validate:
        raise ValueError("Can not add an empty description, please add description")
    return description_to_validate    

    
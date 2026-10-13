from Validations import category_empty
from Movements import FinalMovements
import pytest


def test_valid_category():
    result = category_empty("Food")
    assert result == "Food"


def test_empty_category():
    with pytest.raises(ValueError):
        category_empty("")


def test_none_category():
    with pytest.raises(ValueError):
        category_empty(None)


def test_zero_category():
    with pytest.raises(ValueError):
        category_empty(0)


def test_expense_amount():
    movement = FinalMovements(15000, "Food", "Buy groceries", "Loss")

    assert movement.expense_amount == 15000


def test_category():
    movement = FinalMovements(15000, "Food", "Buy groceries", "Loss")

    assert movement.category == "Food"


def test_movement_description():
    movement = FinalMovements(15000, "Food", "Buy groceries", "Profit")

    assert movement.movement_description == "Buy groceries"


def test_expense():
    movement = FinalMovements(15000, "Food", "Buy groceries", "Profit")

    assert movement.expense == "Profit"        
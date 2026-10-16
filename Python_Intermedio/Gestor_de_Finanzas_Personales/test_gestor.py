from validations import validate_category_empty,validate_category,validate_description_empty,validate_amount_not_less_than_zero,validate_amount
import pytest



def test_valid_category():
    input_valid_category = "Food"

    result_validate_category = validate_category(input_valid_category)

    assert result_validate_category == "Food"


def test_empty_category():
    with pytest.raises(ValueError):
        validate_category_empty("")


def test_valid_amount():
    assert validate_amount("1500") == 1500.0


def test_invalid_amount():
    with pytest.raises(ValueError, match="Amount must be a number"):
        validate_amount("abc")


def test_amount_zero():
    with pytest.raises(ValueError):
        validate_amount_not_less_than_zero(0)


def test_amount_less_than_zero():
    with pytest.raises(ValueError):
        validate_amount_not_less_than_zero(-500)

def test_empty_description():
    with pytest.raises(ValueError):
        validate_description_empty("")

def test_not_empty_description():
    input_not_empty_description = "Food"

    result_not_empty_description = validate_description_empty(input_not_empty_description)

    assert result_not_empty_description == "Food"        
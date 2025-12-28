from src.masks import get_mask_card_number
import pytest


def test_mask_card_number_string():
    """Тест правильной маскировки номера карты со строками"""
    assert get_mask_card_number('1234123412341234') == '1234 12** **** 1234'

def test_mask_card_number_digit():
    """Тест правильной маскировки номера карты с цифрами"""
    assert get_mask_card_number(1234123412341234) == '1234 12** **** 1234'

def test_mask_card_number_invalid__len_number():
    """Тест маскировки номера карты с неправильной длинной номера"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(12341234123412341234)

def test_mask_card_number_empty_number():
    """Тест маскировки номера карты с пустым значением"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number('')

def test_mask_card_number_invalid_incorrect_number():
    """Тест маскировки номера карты с неправильным форматом данных"""
    with pytest.raises(ValueError, match="Неверный формат номера карты"):
        get_mask_card_number('****************')

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number_string():
    """Тест правильной маскировки номера карты со строками"""
    assert get_mask_card_number('1234123412341234') == '1234 12** **** 1234'


def test_mask_card_number_digit():
    """Тест правильной маскировки номера карты с цифрами"""
    assert get_mask_card_number(1234123412341234) == '1234 12** **** 1234'


def test_mask_card_number_invalid_len_number():
    """Тест маскировки номера карты с неправильной длинной номера"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(12341234123412341234)


def test_mask_card_number_empty_number():
    """Тест маскировки номера карты с пустым значением"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number('')


def test_mask_card_number_incorrect_number():
    """Тест маскировки номера карты с неправильным форматом данных"""
    with pytest.raises(ValueError, match="Неверный формат номера карты"):
        get_mask_card_number('****************')


def test_mask_account_string():
    """Тест правильной маскировки номера счета со строками"""
    assert get_mask_account('73654108430135874305') == '**4305'


def test_mask_account_digit():
    """Тест правильной маскировки номера счета с цифрами"""
    assert get_mask_account(73654108430135874305) == '**4305'


def test_mask_account_invalid_len_number():
    """Тест маскировки номера счета с неправильной длинной номера"""
    with pytest.raises(ValueError, match="Номер счета должен состоять из 20 цифр"):
        get_mask_account(1234)
        get_mask_account(123412341234123413241234)


def test_mask_account_empty_number():
    """Тест маскировки номера счета с пустым значением"""
    with pytest.raises(ValueError, match="Номер счета должен состоять из 20 цифр"):
        get_mask_account('')


def test_mask_account_incorrect_number():
    """Тест маскировки номера счета с неправильным форматом данных"""
    with pytest.raises(ValueError, match="Неверный формат номера счета"):
        get_mask_account('********************')

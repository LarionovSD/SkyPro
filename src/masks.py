from typing import Union


def get_mask_card_number(number_card: Union[int, str]) -> Union[int, str]:
    """Функция, маскирующая часть цифр с номера карты"""
    str_number = str(number_card)
    if len(str_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    elif not str_number.isdigit():
        raise ValueError("Неверный формат номера карты")
    mask_number = f"{str_number[0:4]} {str_number[4:6]}** **** {str_number[12:]}"
    return mask_number


def get_mask_account(number_account: Union[int, str]) -> Union[int, str]:
    """Функция, маскирующая часть цифр с номера счета"""
    str_number = str(number_account)
    mask_account = f"**{str_number[-4:]}"
    return mask_account

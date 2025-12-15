from typing import Union


def get_mask_card_number(number_card: int) -> Union[int, str]:
    """Функция, маскирующая часть цифр с номера карты"""
    str_number = str(number_card)
    musk_number = f"{str_number[0:4]} {str_number[4:6]}** **** {str_number[12:]}"
    return musk_number


def get_mask_account(number_account: int) -> Union[int, str]:
    """Функция, маскирующая часть цифр с номера счета"""
    str_number = str(number_account)
    musk_account = f"**{str_number[-4:]}"
    return musk_account

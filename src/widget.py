import re
from typing import Union
from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(number_account_card: Union[int, str]) -> Union[int, str]:
    """Функция, маскирующая номер счета и номер карты"""
    if "Счет" in number_account_card:
        return f"Cчет {get_mask_account(number_account_card)}"
    elif "Счет" not in number_account_card:
        return f"{number_account_card[:-16]}{get_mask_card_number(number_account_card[-16:])}"
  

def get_date(date_string: str) -> str:
    """Функция вывода даты в корректный формат"""
    pattern = r'(\d{2,4})-(\d{2})-(\d{2,4})'
    match = re.search(pattern, date_string)
    part1, part2, part3 = match.groups()
    if len(part1) == 4:
        year, month, day = part1, part2, part3
    else:
        day, month, year = part1, part2, part3
    return f"{day}.{month}.{year}"

from typing import Union
from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(number_account_card: Union[int, str]) -> Union[int, str]:
    if "Счет" in number_account_card:
        return f"Cчет {get_mask_account(number_account_card)}"
    elif "Maestro" in number_account_card:
        return f"Maestro {get_mask_card_number(number_account_card[-16:])}"
    elif "MasterCard" in number_account_card:
        return f"MasterCard {get_mask_card_number(number_account_card[-16:])}"
    elif "Visa Classic" in number_account_card:
        return f"Visa Classic {get_mask_card_number(number_account_card[-16:])}"
    elif "Visa Platinum" in number_account_card:
        return f"Visa Platinum {get_mask_card_number(number_account_card[-16:])}"
    elif "Visa Gold" in number_account_card:
        return f"Visa Gold {get_mask_card_number(number_account_card[-16:])}"


def get_date(str_with_date: str) -> str:
    year = str_with_date[:4]
    month = str_with_date[5:7]
    day = str_with_date[8:10]
    format_date = f"{day}.{month}.{year}"
    return format_date

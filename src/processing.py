from typing import Any, Dict, List


def filter_by_state(list_with_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция для фильтрации списка по значению state"""
    filtered_list: List[Dict[str, Any]] = []
    for element_of_dict in list_with_data:
        if element_of_dict.get("state") == state:
            filtered_list.append(element_of_dict)
    return filtered_list


def sort_by_date(list_with_data: List[Dict[str, Any]], sorting_order: bool = True) -> List[Dict[str, Any]]:
    """Функция для сортировки списка по дате, значение по умолчанию задано - по убыванию"""
    return sorted(list_with_data, key=lambda x: x["date"], reverse=sorting_order)

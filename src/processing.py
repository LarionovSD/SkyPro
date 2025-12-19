def filter_by_state(list_with_data: list, state='EXECUTED') -> list:
    """Функция для фильтрации списка по значению state"""
    filtered_list = []
    for element_of_dict in list_with_data:
        for value in element_of_dict.values():
            if value == state:
                filtered_list.append(element_of_dict)
    return filtered_list


def sort_by_date(list_with_data: list, sorting_order=True):
    """Функция для сортировки списка по дате, значение по умолчанию задано - по убыванию"""
    return sorted(list_with_data, key=lambda x: x["date"], reverse=sorting_order)

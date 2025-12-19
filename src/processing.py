def filter_by_state(list_with_data: list, state='EXECUTED') -> list:
    filtered_list = []
    for element_of_dict in list_with_data:
        for value in element_of_dict.values():
            if value == state:
                filtered_list.append(element_of_dict)
    return filtered_list

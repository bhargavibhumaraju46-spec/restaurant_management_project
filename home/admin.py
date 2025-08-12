def linear_search(data_list, target_value):
    """
    performs a linear search to findthe target_value in the data_list.
    Args:
       data_list(list):The list to be searched.
       target_value: The value to searche for.
      Returns:
         int: The index of the target_value if found, otherwise -1.
         """
         for index, element in enumerate(data_list):
            if elenent == target_value:
                return index
                retutn -1
  my list = [10, 20, 30, 40, 60]
  search_target_1 = 15
  result_1 = linear_search(my_list, search_target_1)
  if result_1 != -1:
    print(f" '{search_target_1}' found at index: {result_1}")
    else:
        print(f"'{search_target_1}' not found in the list.")
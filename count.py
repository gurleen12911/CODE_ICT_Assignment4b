# count.py

def count_total_sum(my_list):
    total_sum = 0
    for element in my_list:
        if isinstance(element, (int, float)):
            total_sum += element
    print(f"Total sum of numeric elements: {total_sum}")

def count_number_of_elements(my_list):
    num_elements = len(my_list)
    print(f"Number of elements in the list: {num_elements}")

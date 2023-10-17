# remove_element.py
def remove_element(my_list, element):
    if element in my_list:
        my_list.remove(element)
        return True
    return False

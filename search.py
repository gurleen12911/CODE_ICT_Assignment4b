# search.py

def search_element(my_list):
    element = input("Enter the element you want to search for: ")

    if any(isinstance(x, int) and x == int(element) for x in my_list):
        print(f"Element '{element}' found in the list.")
    elif any(isinstance(x, float) and x == float(element) for x in my_list):
        print(f"Element '{element}' found in the list.")
    elif element in my_list:
        print(f"Element '{element}' found in the list.")
    else:
        print(f"Element '{element}' not found in the list.")

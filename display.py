def display_list(my_list):
    print("List contents:")
    for element in my_list:
        print(element)

def display_menu():
    print("Menu:")
    print("1. Stop running the program")
    print("2. Search for an element")
    print("3. Add a new element")
    print("4. Remove an element")
    print("5. Sort the list (ascending)")
    print("6. List all elements")
    print("7. Count the total sum of elements")
    print("8. Count the number of elements")
    choice = input("Enter your choice: ")
    return choice

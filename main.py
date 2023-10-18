import random
from display import display_list, display_menu
from search import search_element
from add import add_element
from remove import remove_element
from sort import sort_list
from list import list_elements
from count import count_total_sum, count_number_of_elements
from gui import create_gui

my_list = [random.randint(1, 100) for _ in range(10)]
my_list += [random.uniform(1.0, 100.0) for _ in range(10)]
my_list += [f"String {random.randint(1, 10)}" for _ in range(10)]

#added gui
def create_gui_requested():
    choice = input("Do you want to use the GUI (Y/N)? ").strip().lower()
    return choice == "y"

if __name__ == "__main__":
    display_list(my_list)
    if create_gui_requested():
        create_gui(my_list)
    else:
        while True:
            choice = display_menu()
            if choice == "1":
                print("Exiting the program.")
                break
            elif choice == "2":
                search_element(my_list)
            elif choice == "3":
                add_element(my_list)
            elif choice == "4":
                remove_element(my_list)
            elif choice == "5":
                sort_list(my_list)
            elif choice == "6":
                list_elements(my_list)
            elif choice == "7":
                count_total_sum(my_list)
            elif choice == "8":
                count_number_of_elements(my_list)
            else:
                print("Invalid choice. Please choose a valid option.")

import tkinter as tk
from tkinter import messagebox
import remove 

def create_gui(my_list):
    def search_element_gui():
        element = search_entry.get()
        found = False
        for i, item in enumerate(my_list):
            if str(item) == element:
                listbox.select_set(i)
                found = True
        if not found:
            messagebox.showinfo("Search Result", f"Element '{element}' not found in the list.")

    #functions for menu  choices

    def add_element_gui():
        element = add_entry.get()
        my_list.append(element)
        listbox.insert(tk.END, str(element))

    def remove_element_gui():
        element = remove_entry.get()
        if element:
            try:
                element = float(element)
            except ValueError:
                pass  
            removed = remove.remove_element(my_list, element)
            if removed:
                listbox.delete(0, tk.END)
                for item in my_list:
                    listbox.insert(tk.END, str(item))
            else:
                messagebox.showinfo("Removal Result", f"Element '{element}' not found in the list.")


    def sort_list_gui():
        def custom_sort_key(x):
            if isinstance(x, int):
                return (0, x)
            elif isinstance(x, float):
                return (1, x)
            else:
                return (2, str(x))

        my_list.sort(key=custom_sort_key)
        
        listbox.delete(0, tk.END)
        for item in my_list:
            listbox.insert(tk.END, str(item))


    def list_elements_gui():
        listbox.delete(0, tk.END)
        for element in my_list:
            listbox.insert(tk.END, str(element))

    def count_total_sum_gui():
        total_sum = 0
        for element in my_list:
            if isinstance(element, (int, float)):
                total_sum += element
        messagebox.showinfo("Total Sum", f"Total sum of numeric elements: {total_sum}")

    def count_number_of_elements_gui():
        num_elements = len(my_list)
        messagebox.showinfo("Number of Elements", f"Number of elements in the list: {num_elements}")

    root = tk.Tk()
    root.title("List Program GUI")

    main_frame = tk.Frame(root)
    main_frame.pack()

    list_label = tk.Label(main_frame, text="List contents:")
    list_label.grid(row=0, column=0, columnspan=2)

    listbox = tk.Listbox(main_frame)
    listbox.grid(row=1, column=0, columnspan=2)
    for element in my_list:
        listbox.insert(tk.END, str(element))

    search_label = tk.Label(main_frame, text="Enter the element you want to search for:")
    search_label.grid(row=2, column=0)
    search_entry = tk.Entry(main_frame)
    search_entry.grid(row=2, column=1)
    search_button = tk.Button(main_frame, text="Search", command=search_element_gui)
    search_button.grid(row=2, column=2)

    add_label = tk.Label(main_frame, text="Enter the element you want to add:")
    add_label.grid(row=3, column=0)
    add_entry = tk.Entry(main_frame)
    add_entry.grid(row=3, column=1)
    add_button = tk.Button(main_frame, text="Add Element", command=add_element_gui)
    add_button.grid(row=3, column=2)

    remove_label = tk.Label(main_frame, text="Enter the element you want to remove:")
    remove_label.grid(row=4, column=0)
    remove_entry = tk.Entry(main_frame)
    remove_entry.grid(row=4, column=1)
    remove_button = tk.Button(main_frame, text="Remove Element", command=remove_element_gui)
    remove_button.grid(row=4, column=2)

    sort_button = tk.Button(main_frame, text="Sort List", command=sort_list_gui)
    sort_button.grid(row=5, column=0)

    list_button = tk.Button(main_frame, text="List All Elements", command=list_elements_gui)
    list_button.grid(row=5, column=1)

    count_total_sum_button = tk.Button(main_frame, text="Count Total Sum", command=count_total_sum_gui)
    count_total_sum_button.grid(row=6, column=0)

    count_number_of_elements_button = tk.Button(main_frame, text="Count Number of Elements", command=count_number_of_elements_gui)
    count_number_of_elements_button.grid(row=6, column=1)

    root.mainloop()

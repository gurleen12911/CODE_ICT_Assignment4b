# sort.py

def sort_list(my_list):
    my_list.sort(key=lambda x: (isinstance(x, int), isinstance(x, float), str(x)))

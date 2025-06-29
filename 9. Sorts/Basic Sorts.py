

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
             if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list



print(bubble_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


print(selection_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]

    return my_list


print(insertion_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
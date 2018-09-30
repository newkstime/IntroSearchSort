def bubble_sort(obj_list):
    """
    Code this function.
    The PersonList is the obj_list parameter
    Nothing is returned
    """
    for num in range(len(obj_list) - 1, 0, -1):
        for i in range(num):
            if obj_list[i].compare(obj_list[i+1]) == 1:
                temp = obj_list[i]
                obj_list[i], obj_list[i+1] = obj_list[i+1], obj_list[i]


def binary_search(obj_list, obj):
    """
    Code this function.
    The PersonList is the obj_list parameter
    The Person is the obj
    Return an integer: the index of found object or -1
    """
    min = 0
    max = len(obj_list) - 1
    while True:
        if max < min:
            return -1
        middle = (min + max) // 2
        if obj_list[middle].compare(obj) == -1:
            min = middle + 1
        elif obj_list[middle].compare(obj) == 1:
            max = middle - 1
        else:
            return middle
    #if len(obj_list) >= 1:
    #    middle = len(obj_list) / 2
    #    if obj.compare(obj_list[middle]) == 0:
    #        return middle
    #    elif obj.compare(obj_list[middle]) == -1:
    #        return binary_search(obj_list[:middle], obj)
    #    else:
    #        return binary_search(obj_list[middle+1:], obj)
    #else:
    #    return -1

def linear_search(obj_list, obj):
    """
    Code this function.
    The PersonList is the obj_list parameter
    The Person is the obj
    Return an integer: the index of found object or -1
    """
    #name = str(obj.get_name())
    for i in range(len(obj_list)):
        if obj.compare(obj_list[i]) == 0:
            return i
        elif i == len(obj_list) - 1:
            return -1

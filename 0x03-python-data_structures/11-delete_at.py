#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 and idx == 0:
        return None
    elif (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    else:
        my_list.remove(my_list[idx])
        return my_list

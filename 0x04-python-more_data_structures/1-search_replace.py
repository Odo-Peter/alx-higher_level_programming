#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0 or my_list is None:
        return None
    elif search > len(my_list):
        return
    else:
        new_list = my_list.copy()
        idx = my_list.index(search)
        if idx is None:
            return
        else:
            new_list[idx] = replace
        return new_list

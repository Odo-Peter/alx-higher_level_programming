#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if len(my_list) == 0 or my_list is None:
        return ()
    else:
        idx = new_list_list.index(search)
        new_list[idx] = replace
    return new_list

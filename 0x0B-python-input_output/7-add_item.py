#!/usr/bin/python3
""" Module 7-add_item
that adds all arguments to a Python list, and then
save them to a file
"""

import sys
import os.path

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_array = []
if os.path.exists("add_item.json"):
    my_array = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_array.append(arg)

save_file(my_array, "add_item.json")

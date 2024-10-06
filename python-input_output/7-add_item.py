#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if os.path.isfile("./add_item.json"):
    obj = load_from_json_file("add_item.json")
else:
    obj = []
save_to_json_file(obj + sys.argv[1:], "add_item.json")

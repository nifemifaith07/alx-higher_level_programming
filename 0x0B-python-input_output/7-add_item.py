#!/usr/bin/python3
"""adds all args to a Python List then save as a JSON representation"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

j_file = add_item.json
json_list = []

if os.path.exists(j_file):
    json_list = load_from_json_file(j_file)

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, j_file)

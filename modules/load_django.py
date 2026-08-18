''' Запуск Django всторонней папке'''

import os,json
from pathlib import Path
# from modules.bs4phone_data import dict_specs
dict_specs = {"Name":"Mary","Age":34}

############### Checking the position of initial (parser) file #########
path = Path(__file__)
print("modules", path)
print("json",path.parent)
########### Creating directory and json file in it. #####################
road = path.parent.parent/"json"; print(road)
road.mkdir(parents = True, exist_ok = True)
j_file= road/"res_data_plw.json"
with open(j_file, "w",encoding="utf-8") as f :
    json.dump(dict_specs,f,ensure_ascii = False, indent = 4)

# new_text = new_file.open("w")
# new_text.write(f"--Congratulations!!!-- \n-- This time it worked out!")
######### Checking the existence and address of the json file #############
print(40*"*")
way = Path(j_file)
print(way)

try:
    with open(way,'r') as f:
        new_dict= json.load(f)
        print("✅--Uploaded!--", new_dict)
except Exception as e:
        print(f"❌--- No such file ---")
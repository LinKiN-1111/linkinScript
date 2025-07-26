import os
import sys
import json
script_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(script_path)
data_file_path = os.path.join(root_path,"data","lkarm.txt")

#将存储记录的arm指令从文件中读取到data变量
with open(data_file_path, 'r') as file:
    data = json.load(file)

if(len(sys.argv)!=2):
    print("Usage: python lkarm.py <command>")
    sys.exit(1)

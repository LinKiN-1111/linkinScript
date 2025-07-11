# This script reads the contents of the file "../data/lkcmd" and prints it to
import os
script_dir = os.path.dirname(os.path.abspath(__file__))  # lkcmd.py 的位置
root_dir = os.path.dirname(script_dir)                   # 退到 MYSCRIPT/
file_path = os.path.join(root_dir, "data", "lkcmd.txt")  # 拼接目标路径

with open(file_path, "r") as file:
    print("".join(file.readlines()))

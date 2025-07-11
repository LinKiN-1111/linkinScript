import os
import sys

if len(sys.argv) != 2:
    print("Usage: python open.py <folder_path>")
    sys.exit(1)

# 获取命令行参数中的文件夹路径
folder_path = sys.argv[1]

os.startfile(folder_path)
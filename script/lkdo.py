#具体需求就是调用adb命令,然后获取某个文件夹中的文件列表,然后放到字典中,给用户选择某个文件执行
import subprocess
import os
def list_files_in_directory(directory):
    # 使用adb命令获取目录下的文件列表
    try:
        result = subprocess.run(['adb', 'shell', 'ls', directory], 
                                capture_output=True, text=True, check=True)
        files = result.stdout.splitlines()
        print(files)
        # 解析文件列表并存储到字典中
        file_dict = {}
        i = 0
        for file in files:
            file_dict[i] = file.strip()
            i+=1
                    
        print(file_dict)
        return file_dict
    except subprocess.CalledProcessError as e:
        print(f"Error executing adb command: {e}")
        #直接退出
        exit()

def choose_file(file_dict):
    print("choose a file to execute:")
    for i in range(len(file_dict)):
        print(f"{i}: {file_dict[i]}")

def execute_file(file_name):
    # 使用adb命令执行指定的文件
    try:
        subprocess.run(['adb', 'shell', 'sh', f'/data/local/tmp/{file_name}'],)
    except subprocess.CalledProcessError as e:
        print(f"Error executing adb command: {e}")

file_dict = list_files_in_directory("data/local/tmp/")
choose_file(file_dict)
try:
    file_index = int(input("Enter the index of the file to execute: "))
except ValueError as e:
    print("Invalid input. Please enter a number.")
    exit()

file = file_dict.get(file_index)
if file:
    execute_file(file)
else:
    print("Invalid file index selected.")
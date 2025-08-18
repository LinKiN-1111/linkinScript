#coding=utf-8
import os
script_dir = os.path.dirname(os.path.abspath(__file__))  # lkcmd.py 的位置
root_dir = os.path.dirname(script_dir)                   # 退到 MYSCRIPT/
conda_path = os.path.join(root_dir, "data","lkcoco" ,"coco_conda.txt")  # 拼接目标路径
git_path = os.path.join(root_dir, "data","lkcoco" ,"coco_git.txt")  # 拼接目标路径
frida_path = os.path.join(root_dir, "data","lkcoco" ,"coco_firda.txt")  # 拼接目标路径
docker_path = os.path.join(root_dir, "data","lkcoco" ,"coco_docker.txt")  # 拼接目标路径

print("choose the command you want to know:")
print("1 : git")
print("2 : frida")
print("3 : conda")
print("4 : docker")

choosed = input("please input a number : ")

if(choosed == '1'):
    with open(git_path, "r",encoding='utf-8') as file:
        print("".join(file.readlines()))

if(choosed == '2'):
    with open(frida_path, "r",encoding='utf-8') as file:
        print("".join(file.readlines()))

if(choosed == '3'):
    with open(conda_path, "r",encoding='utf-8') as file:
        print("".join(file.readlines()))

if(choosed == '4'):
    with open(docker_path, "r",encoding='utf-8') as file:
        print("".join(file.readlines()))



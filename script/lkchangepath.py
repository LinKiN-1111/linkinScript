import sys

if len(sys.argv) != 2:
    print("Usage:changepath <filepath>")
    exit()

path = sys.argv[1].upper()

if(":" in path):
    #means windows path convert to wsl2 path
    if("C" in path):
        result = path.replace("C:","/mnt/c")
        result = result.replace("\\","/")
    elif("D" in path):
        result = path.replace("D:","/mnt/d")
        result = result.replace("\\","/")
    elif("F" in path):
        result = path.replace("F:","/mnt/f")
        result = result.replace("\\","/")
    print(result.lower())
else:
    #means wsl2 path convert to windows path
    print("wait for complete")
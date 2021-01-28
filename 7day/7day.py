import re
import glob
filepath = "./wj/*.*"
wb_path_all = glob.glob(filepath)
print(
        wb_path_all
)

def readline_count(file_name):
    return len(open(file_name).readlines())

def extract_string(line):
    matchObj = re.match(r'.*/(.*)', line,  re.M)
    return matchObj.group(1)

if __name__ == '__main__':
    for line in wb_path_all:
       hs = readline_count(line)
       line = extract_string(line)
       print("{} ---  此文件下一共 {} 行代码！".format(line,hs))
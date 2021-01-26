#coding:utf-8
import re
import glob
wb_path = "file/*.txt"
wb_path_all  = glob.glob(wb_path)
zy = ["We","billing","a","are"]

a = 0
ps = 0
for path in wb_path_all:
    ps = ps + 1
    f = open(path)
    for line2 in f:
        pass
    list = line2.split(" ")#将读取到的文件内容以空格分隔然后转为list
    new_list = []
    for i in list:
        matchObj = re.match(r'[a-zA-Z]*', i,  re.M)
        new_list.append(matchObj.group())
    print("new_list{}".format(new_list))
    for i in new_list:
        if i in zy:
            a = a+1
            # print(i)
print("{}篇文章重要的单词出现的次数总共为 {} 次".format(ps,a))

#coding:utf-8
import re
wb_path = "./wb.txt"
zy = ["We","billing","a","are"]
f = open(wb_path)
a = 0
for line2 in f:
    pass
list = line2.split(" ")#将读取到的文件内容以空格分隔然后转为list
new_list = []
for i in list:
    matchObj = re.match(r'[a-zA-Z]*', i,  re.M)
    new_list.append(matchObj.group())

for i in new_list:
    if i in zy:
        a = a+1
        print(i)
print("此文章重要的单词出现的次数为 {} 次".format(a))

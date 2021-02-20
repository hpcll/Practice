#coding=utf-8
import xml.etree.ElementTree as ET
import re
import json
import random
tree = ET.parse("dump.xml")
# 根节点
root = tree.getroot()
# 标签名
print('root_tag:',root.tag)

for child in root:
    str = child[0][0][0][0][0][9].attrib["bounds"]
    # print(str)
s = str.replace('][','] [')#替换][为 ] [  方便转list
files = s.split(' ') # 用,号分割成list
print(files)
matchObj = re.findall(r'.*\[(.*?),(.*?)]', files[0])
matchObj1 = re.findall(r'.*\[(.*?),(.*?)]', files[1])
x = int(matchObj[0][0])
y = int(matchObj[0][1])
x1 = int(matchObj1[0][0])
y1 = int(matchObj1[0][1])
print(x,y,x1,y1)
x2 = random.randint(x, x1)
y2 = random.randint(y,y1)
print(x2,y2)




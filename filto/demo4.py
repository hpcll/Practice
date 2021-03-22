#coding=utf-8
import xml.etree.ElementTree as ET
import xml
import re
import json
import random
tree = ET.parse("dump.xml")
# 根节点
root = tree.getroot()
# 标签名
print('root_tag:',root.tag)

for ele in root:
    if ele[0][0][0][0][0][9].attrib["text"] == "视频":
        break
    else:
        for ele1 in ele:
            print("哈哈哈哈")




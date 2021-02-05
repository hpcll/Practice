import re
import os
#
htmlpath = "./baidu.html"
wb = open(htmlpath)
list = []
for line in wb:
    list.append(line)
wb = "".join(list)
zw = re.search('.*<body>(.*)</body>*', wb, re.M|re.S )
print(zw.group(1))

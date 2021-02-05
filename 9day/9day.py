import re

htmlpath = "./baidu.html"
wb = open(htmlpath)
list = []
for line in wb:
    list.append(line)
wb = "".join(list)
zw = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", wb, re.M|re.S )
#http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
print(zw)
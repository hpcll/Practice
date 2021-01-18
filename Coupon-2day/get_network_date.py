import datetime
import re
import time
from datetime import datetime
import requests

# 设置头信息，没有访问会错误400！！！
hea = {'User-Agent': 'Mozilla/5.0'}
# 设置访问地址，我们分析到的；
url = r'http://time1909.beijing-time.org/time.asp'
# 用requests get这个地址，带头信息的；
r = requests.get(url=url, headers=hea)
tm = r.text

def data(a):
    return re.findall(r"=(.*)", a)[0]

def time_str():
    list = tm.split(";")
    date = [None] * (len(list) - 2)
    for i in range(1, len(list) - 1):
        date[i - 1] = data(list[i])
    return date

def Network_time():
    date = time_str()
    list1 = ["year", "month", "day", "hour", "minute", "second", "week"]
    Dict = dict(zip(list1, date))
    year = Dict['year']
    month = Dict['month']
    day = Dict['day']
    week = Dict['week']
    hour = Dict['hour']
    minute = Dict['minute']
    second = Dict['second']

    Network_time = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second  # 字符串格式的时间
    time_stamp = time.mktime(time.strptime(Network_time, '%Y-%m-%d %H:%M:%S'))  # 当前时间的时间戳
    # # return year, month, day, hour, minute, seccond, week
    Network_time_format = datetime.strptime(Network_time, '%Y-%m-%d %H:%M:%S')  # 时间格式的时间
    return Network_time, time_stamp, Network_time_format, dict

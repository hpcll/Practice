import os
import re
#原坐标的手机分辨率
old_res_x = 1080
old_res_y = 2340


def cilke(x,y):
    os.system('adb devices')
    return os.system('adb shell input tap {} {}'.format(x,y))

def iphone_info():
    with os.popen('adb shell wm size') as f:
        text = f.read()
    matchObj = re.match(r'.*: (.*)x(.*)?', text, re.M)
    new_res_x = int(matchObj.group(1))
    new_res_y = int(matchObj.group(2))
    return new_res_x,new_res_y


"""
new_x = 187*1024/1920#new_x = x*old_res_x/new_res_x
new_y = 567*768/1080#new_y = y*old_res_y/new_res_y
"""

def res_convert(x,y):
    """坐标换算"""
    new_res_x = int(iphone_info()[0])
    new_res_y = int(iphone_info()[1])
    new_x = x * old_res_x / new_res_x
    new_y = y * old_res_y / new_res_y
    return new_x,new_y

if __name__ == '__main__':
    if old_res_x == iphone_info()[0] and old_res_y == iphone_info()[1]:
        cilke(124,567)
        print("当前的手机分辨率为:1080*2340")
    else:
        cilke(res_convert(124, 567)[0],res_convert(124, 567)[1])
        print("当前手机分辨率为:{}*{}".format(iphone_info()[0],iphone_info()[1]))
import time
import os
import re


old_res_x = 1080
old_res_y = 2340


def cilke(x,y):
    x1,y1 = res_convert(x,y)
    # os.system('adb devices')
    os.system('adb shell input tap {} {}'.format(x1,y1))


def Screenshot_img(mz):
    os.system('adb shell screencap -p /sdcard/{}.png'.format(mz))#截图保存至手机SD卡根目录
    os.system('adb pull /sdcard/{}.png /Users/hupc/Desktop/{}.png'.format(mz,mz))#将问件从手机pull到电脑

def join_home_page():
    # os.system('adb devices') #获取连接设备
    os.system('adb shell am force-stop com.video.editor.filto ')#杀死 app
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')#打开app首页
    time.sleep(1)
    print("正在保存首页截图。。。。")
    Screenshot_img('home')
    time.sleep(3)


def join_stting_page():#进入设置页面
    join_home_page()
    cilke(78, 200)
    # os.system('adb shell input tap 76 200')#点击设置按钮
    time.sleep(1)
    print("正在保存设置页截图。。。。")
    Screenshot_img('stting')
    time.sleep(3)

def iphone_info():
    with os.popen('adb shell wm size') as f:
        text = f.read()
    matchObj = re.match(r'.*: (.*)x(.*)?', text, re.M)
    new_res_x = int(matchObj.group(1))
    new_res_y = int(matchObj.group(2))
    return new_res_x, new_res_y

def res_convert(x, y):
    """坐标换算"""
    new_res_x, new_res_y = iphone_info()
    new_x = x * old_res_x / new_res_x
    new_y = y * old_res_y / new_res_y
    return new_x, new_y

if __name__ == '__main__':
    join_stting_page()

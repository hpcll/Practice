#coding:utf-8
import os
import time
import re
"""
大概思路：
1.输入本次需要检查的 多国文案 界面的 Activity
2.自动切换语言，然后打开需要检查的页面
3.将当前页面截图
4.最后人工对比
目的：减去每次切语言的麻烦
首页：com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash
splash：
相册页：com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivityMediaSelect
后门页面：com.video.editor.filto/com.gameinlife.color.paint.filto.test.ActivitySetting
"""
"""#首页按钮
os.system('adb shell input tap 768 1981')#首页点击图片按钮
os.system('adb shell input tap 76 200')#进入设置页面
os.system('adb shell input keyevent 4')#点击back键回到首页
os.system('adb shell input tap 305 1981')#点击首页视频按钮，进入视频选择页
#相册页
os.system('adb shell input tap 540 772')#选择视频进入视频编辑页
#编辑页通用
os.system('adb shell input tap 90 239')#点击编辑页的返回按钮X
os.system('adb shell input tap 908 223')#点击编辑页的保存按钮
#视频编辑页
os.system("adb shell input tap 407 2271")#视频编辑页的特效
os.system('adb shell input tap 139 2259')#视频编辑页的剪辑按钮
os.system('adb shell input tap 113 1860')#视频剪辑页的返回按钮
os.system("adb shell input tap 961 1834")#视频剪辑页的保存按钮
os.system("adb shell input tap 673 2269")#视频剪辑页的保存按钮
os.system("adb shell input tap 681 2282")#视频编辑页的特效
os.system("adb shell input tap 906 2260")#视频编辑页的特效
#图片编辑页
os.system("adb shell input tap 262 2277 ")#图片编辑页滤镜
os.system("adb shell input tap 779 2256 ")#图片编辑页滤镜
#分享页
os.system("adb shell input tap 88 191 ")#分享页返回按钮
os.system("adb shell input tap 964 178 ")#分享页主页按钮
os.system("adb shell input tap 142 2151 ")#分享页ins
os.system("adb shell input tap 341 2151 ")#分享页tiktok
os.system("adb shell input tap 544 2151 ")#分享页snapchat
os.system("adb shell input tap 730 2151 ")#分享页facebook
os.system("adb shell input tap 936 2151 ")#分享页更多
#切换语言对应的坐标
os.system("adb shell input tap 470 611 ")#切换语言
os.system('adb shell input tap 527 619')#德语
os.system('adb shell input tap 527 750')#英语
os.system('adb shell input tap 527 884')#西班牙语
os.system('adb shell input tap 527 1035')#法语
os.system('adb shell input tap 527 1148')#意大利语
os.system('adb shell input tap 527 1281')#日语
os.system('adb shell input tap 527 1412')#韩语
os.system('adb shell input tap 527 1543')#葡萄牙语
os.system('adb shell input tap 527 1675')#俄语
os.system('adb shell input tap 527 1807 ')#中文简体
os.system('adb shell input tap 527 1937')#中文繁体
os.system('adb shell input tap 520 2224')#应用
"""

def open_option():
    os.system('adb shell am force-stop com.video.editor.filto ')  # 杀死 app
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.test.ActivitySetting')  # 打开app首页


#截图
def Screenshot_img(mz):
    os.system('adb shell screencap -p /sdcard/{}.png'.format(mz))#截图保存至手机SD卡根目录
    os.system('adb pull /sdcard/{}.png /Users/hupc/Desktop/{}.png'.format(mz,mz))#将问件从手机pull到电脑

def join_home_page():
    os.system('adb devices') #获取连接设备
    os.system('adb shell am force-stop com.video.editor.filto ')#杀死 app
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')#打开app首页
    time.sleep(1)
    print("正在保存首页截图。。。。")
    Screenshot_img('home')
    time.sleep(3)


def join_stting_page():#进入设置页面
    join_home_page()
    os.system('adb shell input tap 76 200')#点击设置按钮
    time.sleep(1)
    print("正在保存设置页截图。。。。")
    Screenshot_img('stting')
    time.sleep(3)


def join_video_select_page():#进入视频选择页
    join_home_page()
    os.system('adb shell input tap 305 1981')  # 点击首页视频按钮，
    time.sleep(1)
    print("正在保存视频相册页截图。。。。")
    Screenshot_img('video_page')
    time.sleep(3)


def join_photo_select_page():#进入图片选择页
    join_home_page()
    os.system('adb shell input tap 768 1981')  # 首页点击图片按钮
    time.sleep(1)
    print("正在保存图片相册页截图。。。。")
    Screenshot_img('photo_page')
    time.sleep(3)


def join_video_edit():
    join_video_select_page()
    os.system('adb shell input tap 540 772')  # 选择视频进入视频编辑页
    time.sleep(1)
    # os.system('adb shell input tap 90 239')  # 点击编辑页的返回按钮X
    # os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    print("正在保存视频编辑页页截图。。。。")
    Screenshot_img('video_deit_Filter')#视频页，滤镜页面截图
    time.sleep(3)


def join_photo_edit():
    join_photo_select_page()
    os.system('adb shell input tap 540 772')  # 选择图片进入图片编辑页
    time.sleep(1)
    # os.system('adb shell input tap 90 239')  # 点击编辑页的返回按钮X
    # os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    print("正在保存图片编辑页截图。。。。")
    Screenshot_img('phtot_deit_Filter')  # 视频页，滤镜页面截图
    time.sleep(3)


def join_share_page():
    join_photo_edit()
    os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    time.sleep(5)
    print("正在保存分享页截图。。。。")
    Screenshot_img('share_page')  # 视频页，滤镜页面截图


if __name__ == '__main__':
    join_home_page()#打开首页并截图
    join_share_page()#打开分享页并截图，会截4张图。分别是：home.png,photo_page.png,
    join_stting_page()#打开设置页
    join_photo_edit()#打开打开图片编辑页
    join_video_edit()#打开视频编辑页
    join_photo_select_page()#打开图片选择页
    join_video_select_page()#打开视频选择页






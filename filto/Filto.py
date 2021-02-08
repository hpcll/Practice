import time
import os
import re

old_res_x = 1080
old_res_y = 2340

dict = {"DE":[527,619],"EN":[527,750],"ES":[527,884],"FR":[527,1035],
        "IT":[527,1148],"JP":[527,1281],"KR":[527,1412],
        "PT":[527,1543],"BE":[527,1675],"ZH_HK":[527,1937],"ZH_CN":[527,1807]}

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


def click(x,y):
    x1,y1 = res_convert(x,y)
    # os.system('adb devices')
    os.system('adb shell input tap {} {}'.format(x1,y1))


def mkdir(path):
    folder = os.path.exists("/Users/hupc/Desktop/photo/{}".format(path))
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs("/Users/hupc/Desktop/photo/{}".format(path))  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")


def Screenshot_img(lg,mz):
    os.system('adb shell screencap -p /sdcard/{}{}.png'.format(lg,mz))#截图保存至手机SD卡根目录
    os.system('adb pull /sdcard/{}{}.png /Users/hupc/Desktop/photo/{}/{}{}.png'.format(lg,mz,mz,lg,mz))#将文件从手机pull到电脑
    time.sleep(1)

def join_home_page(lg):
    # # os.system('adb devices') #获取连接设备
    # os.system('adb shell am force-stop com.video.editor.filto ')#杀死 app
    # os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')#打开app首页
    time.sleep(1)
    print("正在保存首页截图。。。。")
    mkdir('home')
    Screenshot_img(lg,'home')
    time.sleep(3)


def join_stting_page(lg):#进入设置页面
    click(78, 200)
    # os.system('adb shell input tap 76 200')#点击设置按钮
    time.sleep(1)
    print("正在保存设置页截图。。。。")
    mkdir('stting')
    Screenshot_img(lg,'stting')
    time.sleep(3)

def join_video_select_page(lg):#进入视频选择页
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')  # 打开app首页
    # os.system('adb shell input tap 305 1981')  # 点击首页视频按钮，
    click(305,1981)# 点击首页视频按钮，
    time.sleep(1)
    print("正在保存视频相册页截图。。。。")
    mkdir('video_page')
    Screenshot_img(lg,'video_page')
    time.sleep(3)

def join_photo_select_page(lg):  # 进入图片选择页
    # os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')  # 打开app首页
    # os.system('adb shell input tap 768 1981')  # 首页点击图片按钮
    click(768,1981)
    time.sleep(1)
    print("正在保存图片相册页截图。。。。")
    mkdir('photo_page')
    Screenshot_img(lg,'photo_page')
    time.sleep(3)

def join_video_edit(lg):
    join_video_select_page(lg)
    # os.system('adb shell input tap 540 772')  # 选择视频进入视频编辑页
    click(540,772)
    time.sleep(1)
    # os.system('adb shell input tap 90 239')  # 点击编辑页的返回按钮X
    # os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    print("正在保存视频编辑页页截图。。。。")
    mkdir('video_edit')
    Screenshot_img(lg,'video_deit')#视频页，滤镜页面截图
    time.sleep(3)

def join_photo_edit(lg):
    join_photo_select_page(lg)
    # os.system('adb shell input tap 540 772')  # 选择图片进入图片编辑页
    click(540,772)
    time.sleep(1)
    # os.system('adb shell input tap 90 239')  # 点击编辑页的返回按钮X
    # os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    print("正在保存图片编辑页截图。。。。")
    mkdir('photo_edit')
    Screenshot_img(lg,'photo_edit')  # 视频页，滤镜页面截图
    time.sleep(3)

def join_share_page(lg):
    join_photo_edit(lg)
    click(908,223)
    # os.system('adb shell input tap 908 223')  # 点击编辑页的保存按钮
    time.sleep(5)
    print("正在保存分享页截图。。。。")
    mkdir('share_page')
    Screenshot_img(lg,'share_page')  # 分享页截图
    time.sleep(2)


def Language(x,y):
    click(490,600)
    # os.system("adb shell input tap 490 600 ")
    click(x,y)
    # os.system('adb shell input tap 520 2224')  # 应用
    click(520,2224)

def open_option():
    os.system('adb shell am force-stop com.video.editor.filto ')  # 杀死 app
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.test.ActivitySetting')  # 打开app后门页面

def open_app():
    os.system('adb shell am force-stop com.video.editor.filto ')  # 杀死 app
    os.system('adb shell am start com.video.editor.filto/com.gameinlife.color.paint.filto.activity.ActivitySplash')  # 打开app首页


if __name__ == '__main__':
    for key in dict:
        value = dict[key]
        x, y = value
        open_option()#打开app后门页
        # open_app()#启动APP
        time.sleep(1)
        Language(x, y)
        join_home_page(key)  # 打开首页并截图
        # join_share_page(key)  # 打开分享页并截图，会截4张图。分别是：home.png,photo_page.png,
        # join_stting_page(key)  # 打开设置页
        # join_photo_edit(key)  # 打开打开图片编辑页
        # join_video_edit(key)  # 打开视频编辑页
        # join_photo_select_page(key)  # 打开图片选择页
        # join_video_select_page(key)  # 打开视频选择页

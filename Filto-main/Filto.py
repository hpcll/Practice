import uiautomator2 as u2
from time import sleep
import os
import random
import re

"""
Screenshot_img(self):截图
open_setting(self)：进入设置页
open_Subscribe(self)：进入订阅面
swipe_home(self):滑动首页素材
join_edit(self):进入编辑页
edit_save(self):进入保存页
quit_edit(self):退出编辑页
join_share(self):进入分享页
"""


# import os
# os.path.isfile('test.txt') #如果不存在就返回False
# os.path.exists(path) #如果目录不存在就返回False



def Screenshot_img(device_name, mz):
    """截图"""
    path = '{}/screenshots/{}'.format(os.getcwd(), device_name)
    if os.path.exists(path):
        print("{}截图中。。。".format(mz))
        d.screenshot('{}/{}.png'.format(path, mz))
        print("{}截图完成.....".format(mz))
    else:
        os.makedirs(path)
        print("{}截图中。。。".format(mz))
        d.screenshot('{}/{}.png'.format(path, mz))
        print("{}截图完成.....".format(mz))

    #


# def Screenshot_img(mz):
#     os.system('adb shell screencap -p /sdcard/{}.png'.format(mz))#截图保存至手机SD卡根目录
#     time.sleep(5)
#     os.system('adb pull /sdcard/{}.png {}/screenshots/{}.png'.format(mz,os.getcwd(),mz))#将文件从手机pull到电脑
#     time.sleep(1)



def open_setting(device_name):
    """从首页进入设置页"""
    d(resourceId="com.video.editor.filto:id/iv_home_setting").click()  # 打开设置
    sleep(1)
    Screenshot_img(device_name, "设置")
    d(resourceId="com.video.editor.filto:id/iv_setting_back").click()  # 关闭设置页
    print("回到首页")
    sleep(0.5)


def open_Subscribe(device_name):
    """从首页进入订阅面"""
    d(resourceId="com.video.editor.filto:id/iv_home_pro").click()  # 点击首页 订阅入口
    sleep(1)
    Screenshot_img(device_name, "订阅面")
    d(resourceId="com.video.editor.filto:id/iv_sub_cancel").click()  # 关闭订阅入口
    print("返回首页")


def swipe_home(device_name, direction):
    """滑动首页素材"""
    i = 1
    a = random.randint(1, 7)
    while i < a:
        i = i + 1
        d.swipe_ext(direction, scale=0.8)  # 像右滑动素材  左：left  右：right
    print("总共滑动了{}次".format(a))
    Screenshot_img(device_name, "首页素材")


def join_edit(device_name):
    """进入相册，并选择图片或视频后进入编辑页"""
    d(resourceId="com.video.editor.filto:id/tv_item_use_now").click()  # 点击使用预设
    while True:
        if d(resourceId='com.video.editor.filto:id/media_tab_tv').exists:  # 判断是否加载完成 返回ture
            sleep(1)
            Screenshot_img(device_name, "相册页")
            d.xpath(
                '//*[@resource-id="com.video.editor.filto:id/rl_media"]/android.view.ViewGroup[1]').click()  # 点击相册页的第一个元素
            sleep(1)
            Screenshot_img(device_name, "编辑页")
            break


def quit_edit(device_name):
    """退出编辑页"""
    d(resourceId="com.video.editor.filto:id/iv_edit_back").click()  # 退出编辑页
    while True:
        if d(resourceId="android:id/message").exists:  # 判断是否加了特效
            sleep(1)
            Screenshot_img(device_name, "退出编辑页弹框")
            d(resourceId="android:id/button1").click()  # 确认退出
        else:
            break
    sleep(1)


def edit_save(device_name):
    """编辑完成后点击保存"""
    d(resourceId="com.video.editor.filto:id/tv_edit_save").click()  # 点击保存
    while True:
        if d(resourceId="com.video.editor.filto:id/tv_sub_top").exists:  # 判断特效或滤镜是否收费，是否跳转到了订阅面
            sleep(1)
            Screenshot_img(device_name, "收费弹窗")
            d(resourceId="com.video.editor.filto:id/iv_sub_cancel").click()  # 退出订阅面
            sleep(1)
            d(resourceId="com.video.editor.filto:id/tv_edit_pro_remove_effect").click()  # 移除付费项
            sleep(1)
            d(resourceId="com.video.editor.filto:id/tv_edit_save").click()  # 点击保存
            sleep(1)
            Screenshot_img(device_name, "保存中页面")
            break
        elif d(text="保存中").exists:
            sleep(1)
            Screenshot_img(device_name, "保存中页面")
            break


def join_share(device_name):
    """分享页"""
    while True:
        if d(resourceId="com.video.editor.filto:id/vv_media").exists:# 判断是否保存完成
            if d(resourceId="com.video.editor.filto:id/tv_rate_us_content").exists:
                Screenshot_img(device_name, "评论弹框")
                d(resourceId="com.video.editor.filto:id/iv_rate_us_cancel").click()
                d.sleep(2)
                print("保存完成")
                Screenshot_img(device_name, "分享页")
                d(resourceId="com.video.editor.filto:id/iv_share_back_home").click()  # 返回首页
                print("返回首页")
                break
            else:
                d.sleep(2)
                Screenshot_img(device_name, "分享页")
                d(resourceId="com.video.editor.filto:id/iv_share_back_home").click()  # 返回首页
                print("返回首页")
                break



def get_device_list():
    """获取设备ID"""
    msg = os.popen("adb devices -l").read()
    msg1 = os.popen("adb devices ").read()
    print(msg)
    deviceId = re.findall(r'([\w]+)\tdevice', msg1)
    deviceId_name = re.findall(r"device.*model:(.*)\sdevice", msg)
    return deviceId, deviceId_name


def is_first_open_app():
    """Splsh页面"""
    if d(resourceId="com.video.editor.filto:id/tv_title").wait(timeout=1.0):
        d(resourceId="com.video.editor.filto:id/tv_guide_next").click()
        d(resourceId="com.video.editor.filto:id/tv_guide_next").click()


def get_limit():
    os.popen("adb shell pm grant com.video.editor.filto android.permission.READ_EXTERNAL_STORAGE android.permission.READ_EXTERNAL_STORAGE")


def install_app():
    # 本地路径安装
    wct = d.watch_context()
    wct.when("继续安装").click()
    d.app_install('/Users/hupc/Desktop/filto_1.4_28_03-24-21-33.apk')
    wct.stop()
    # if d(resourceId="com.miui.securitycenter:id/desc").wait(timeout=3.0):
    #     d(resourceId="android:id/button2").click()
    # url 安装
    # d.app_install('http://s.toutiao.com/UsMYE/')


def run_all():
    is_first_open_app()#判断是否第一次打开app
    open_setting(device_name)  # 进入设置页
    open_Subscribe(device_name)  # 进入订阅面
    swipe_home(device_name, "right")  # 滑动首页素材   左：left  右：right
    join_edit(device_name)  # 进入编辑页
    # quit_edit(device_name)#退出编辑页
    edit_save(device_name)  # 点击保存
    join_share(device_name)  # 进入分享页


if __name__ == '__main__':
    device_list = get_device_list()
    deviceId = device_list[0]
    deviceId_name = device_list[1]
    for i in range(0, len(deviceId)):
        device_name = deviceId_name[i]
        deviceid = deviceId[i]
        # 手机的IP
        d = u2.connect(deviceid)
        print("当前连接的设备: {}_{}   设备ID为: {}".format(d.device_info["brand"], device_name, deviceid))
        install_app()
        #授予filto读写权限
        get_limit()
        # 启动App
        d.app_start("com.video.editor.filto")
        run_all()
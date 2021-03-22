import uiautomator2 as u2
from time import sleep
import os
import re


#读取设备状态
msg = os.popen("adb devices").read()
print(msg)

# 正则表达式匹配出 id 信息
if msg == 'List of devices attached\n\n':
    print("设备未连接，请连接设备后重试")
else:
    deviceId = re.findall(r'([\w]+)\tdevice', msg)
    # # 手机的IP
    # d = u2.connect(deviceId)
    # # 启动App
    # d.app_start("com.video.editor.filto",stop=True)
    #
    # sleep(1)

    print(deviceId)


def MultiDevice(d):  # 功能执行
    d.screen_on()
    # print(d.info)
    d.screen_off()

def connect_device(deviceId):
    d = u2.connect(deviceId)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    # MultiDevice(d)
    print(d.screen_on())


# if __name__ == '__main__':
#     d = connect_device()






# def Click(data):
#     d(resourceId=data).click()
# def Xpath(data):
#     d.xpath(data).click()
# def Screenshot_img(file_name):
#     d.screenshot('{}.png'.format(file_name))
#
# #打开设置
# Click('com.video.editor.filto:id/imageView4')
# Xpath('//*[@resource-id="com.video.editor.filto:id/rl_media"]/android.view.ViewGroup[1]')

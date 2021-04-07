import uiautomator2 as u2
import os
import re



def MultiDevice(d):  # 功能执行
    d.screen_on()
    d.screen_off()

def connect_device(deviceId):
    d = u2.connect(deviceId)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    MultiDevice(d)
    print(d.screen_on())

if __name__ == '__main__':
    # 读取设备状态
    msg = os.popen("adb devices").read()
    print(msg)
    # 正则表达式匹配出 id 信息
    if msg == 'List of devices attached\n\n':
        print("设备未连接，请连接设备后重试")
    else:
        deviceId = re.findall(r'([\w]+)\tdevice', msg)
        print("一共连接了{}个设备:{}".format(len(deviceId), deviceId))
    connect_device(deviceId[0])
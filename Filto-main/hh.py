import sys
import uiautomator2  as u2
from time import sleep
import os
import subprocess
import threading
import time

def MultiDevice( d):  # 功能执行

    d.screen_on()
    # print(d.info)
    d.screen_off()

def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()# 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    print(out)
    print((out)[1:-1])
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        print(device)
        devices.append(device)
    return devices  # 手机设备列表



def test_xxx(i):
    d = u2.connect(i)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    MultiDevice(d)


def start():
        threads = []
        for i in range(len(getphonelist())):
            threads.append(threading.Thread(target=test_xxx(getphonelist()[i]),args=()))
        for t in threads:
            time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()
if __name__ == '__main__':
    # start()
    print(getphonelist())

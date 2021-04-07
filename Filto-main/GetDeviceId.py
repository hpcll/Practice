import re
import os

msg = os.popen("adb devices -l").read()
msg1 = os.popen("adb devices ").read()
print(msg)
deviceId = re.findall(r'([\w]+)\tdevice', msg1)
deviceId_name = re.findall(r"device.*model:(.*)\sdevice", msg)
print(deviceId_name,deviceId)
for i in range(0,len(deviceId)):
    print("设备名{},设备ID{}".format(deviceId_name[i],deviceId[i]))

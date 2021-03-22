import re
import os

msg = "List of devices attached\n"\
        "32caf2b1	device\n"\
        "867df495	device"
print(msg)
deviceId = re.findall(r'([\w]+)\tdevice', msg)
print(deviceId)
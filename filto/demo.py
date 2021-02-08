import os
import re
# os.system("adb shell input tap 470 611 ")#切换语言
# os.system('adb shell input tap 527 619')#德语
# os.system('adb shell input tap 527 750')#英语
# os.system('adb shell input tap 527 884')#西班牙语
# os.system('adb shell input tap 527 1035')#法语
# os.system('adb shell input tap 527 1148')#意大利语
# os.system('adb shell input tap 527 1281')#日语
# os.system('adb shell input tap 527 1412')#韩语
# os.system('adb shell input tap 527 1543')#葡萄牙语
# os.system('adb shell input tap 527 1675')#俄语
# os.system('adb shell input tap 527 1937')#中文繁体
# os.system('adb shell input tap 527 1807 ')#中文简体
# os.system('adb shell input tap 530 1937')#应用

#
# dict = {"DE":[527,619],"EN":[527,750],"ES":[527,884],"FR":[527,1035],
#         "IT":[527,1148],"JP":[527,1281],"KR":[527,1412],
#         "PT":[527,1543],"BE":[527,1675],"ZH_HK":[527,1937],"ZH_CN":[527,1807]}
#
# for key in dict:
#     value = dict[key]
#     x,y = value

old_res_x = 1080
old_res_y = 2340


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

os.system("""adb exec-out uiautomator dump /dev/tty | awk '{gsub("UI hierchary dumped to: /dev/tty", "");print}'""")
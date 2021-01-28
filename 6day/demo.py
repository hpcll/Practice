import re

line = "./wj/冒泡.py"

matchObj = re.match(r'.*/(.*)', line,  re.M)#只提取字符串中的字母
line1 = matchObj.group(1)#将提取的字符串赋值给变量 line1
print(line1)
# re模块的使用
"""
re.search(pattern, string, flags=0)
正则匹配
#各参数含协议
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
    flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
    re.I 忽略大小写
    re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    re.M 多行模式
    re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
    re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
    re.X 为了增加可读性，忽略空格和 # 后面的注释


"""
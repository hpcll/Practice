import re

line = "settings7"

matchObj = re.match(r'[a-zA-Z]*', line,  re.M)
print(matchObj.group())
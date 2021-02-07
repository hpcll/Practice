#适配不同的分辨率
import re
X1,Y1 = 1920,1080#修改为编写和调试原始脚本的显示器系统的分辨率的值

X2,Y2 = 1024,768 #后续移植到其他平台时的显示器系统的分辨率的值

f = open('coords.txt').readlines()

s = "transfer coords:"

with open('coords.txt','a') as h:

    h.write('\n'*2+ s + '\n'*2)

for i in f:
    a1 = i.find('(')

    b1 = i.find(',')

    c1 = i.find(')')

    x1 = i[(a1+1):b1]

    y1 = i[(b1+1):c1]

    if bool(re.search(r'\d',i)): #筛选出包含数字的行

        x = int(x1)*X2/X1

        y = int(y1)*Y2/Y1

        j = i.replace(x1,str(int(x)))

        k = j.replace(y1,str(int(y)))

        print (k)
        with open('f:\coords.txt','a') as h: #追加写入文本
            h.write(k)


#coding:utf-8
wb_path = "./wb.txt"

f = open(wb_path)
i = 0

for line2 in f:
    print(line2)

list = line2.split(" ")#将读取到的文件已空格分隔然后转为list
print("此篇文章的单词字数为 {}".format(len(list)))

# a = 0
# for i in list:
#     a = a+1
# print("此篇文章的单词字数为{}".format(a))
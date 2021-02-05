import random

list = [chr(i) for i in range(48, 57)]  # 0-9
list1 = [chr(i) for i in range(97, 123)]  # 小写字母
list2 = [chr(i) for i in range(65, 90)]  # 大写字母
list3 = list + list1 + list2

#随机字符

def ranchar():
    zf = random.sample(list3, 4)
    coupon_id = "".join(zf)  # list转字符串
    return coupon_id

def rancolor():
    print(random.randint(64,255))

if __name__ == '__main__':
    rancolor()

import redis
import random
list4  = "12"
list = [chr(i) for i in range(48, 57)]  # 0-9
list1 = [chr(i) for i in range(97, 123)]  # 小写字母
list2 = [chr(i) for i in range(65, 90)]  # 大写字母
list3 = list + list1 + list2



def coupon():
    """将list3里面的字符，取16位，随机组成list，并将list转为字符串"""
    zf = random.sample(list3,16)
    coupon_id = "".join(zf)#list转字符串
    return coupon_id


if __name__ == '__main__':
    r = redis.Redis(host='127.0.0.1', port=6379,password='1', decode_responses=True)  # 连接redis
    coupon_id_list = []
    for i in range(1,201):
        coupon_id = coupon()
        coupon_id_list.append(coupon_id)
        print("第{}优惠码-------{}".format(i,coupon_id))
        r.set(i,coupon_id)
    print(r.get(200))
    print(r.keys(1))
    print(coupon_id_list)


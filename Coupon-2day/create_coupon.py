

#随机生成16位的优惠码，并将它存入数据库

import random
import pymysql
import datetime
from get_network_date import Network_time
list4  = "12"
list = [chr(i) for i in range(48, 57)]  # 0-9
list1 = [chr(i) for i in range(97, 123)]  # 小写字母
list2 = [chr(i) for i in range(65, 90)]  # 大写字母
list3 = list + list1 + list2


def mysql_info(sql,data):
    db = pymysql.connect(host = "47.242.147.185",
                         database = "mysql",
                         user="root",
                         password = "",
                         charset = "utf8")
    cursor = db.cursor()
    # sql = "insert into coupon values(%s,%s);"
    # data = [count, coupon_id]
    cursor.execute(sql, data)#输入语句
    db.commit()#点击提交
    data = cursor.fetchall()
    # 关闭
    cursor.close()
    db.close()
    return data



def coupon():
    zf = random.sample(list3,16)
    coupon_id = "".join(zf)#list转字符串
    return coupon_id


if __name__ == '__main__':
    now = Network_time()[2]
    # print(type(now))
    delta = datetime.timedelta(days=7)
    n_days = now + delta
    # print(n_days)
    Expired_date = n_days.strftime('%Y-%m-%d %H:%M:%S')
    # print(type(Expired_date))
    count = 0
    new_list = []
    while count < 200:
        coupon_id = coupon()
        # count = count + 1
        sql = "insert into coupon (coupon_id,Expired_date) values(%s,%s)"
        data = [coupon_id,Expired_date]
        try:
            mysql_info(sql,data)
        except Exception as err:
            err = str(err)  # 先将err转为str
            print(err)
            result = err.find('Duplicate entry.*for key.*PRIMARY')
            # count = count - 1
            continue
        new_list.append(coupon_id)
        count = count + 1
        print("第{}个优惠码 ---------     {}".format(count,coupon_id))
    print(new_list)

import filto.Filto as bs
import time

dict = {"DE":[527,619],"EN":[527,750],"ES":[527,884],"FR":[527,1035],
        "IT":[527,1148],"JP":[527,1281],"KR":[527,1412],
        "PT":[527,1543],"BE":[527,1675],"ZH_HK":[527,1937],"ZH_CN":[527,1807]}

if __name__ == '__main__':
    for key in dict:
        value = dict[key]
        x, y = value
        bs.open_option()
        time.sleep(1)
        bs.Language(x, y)
        bs.join_home_page(key)  # 打开首页并截图
        bs.join_share_page(key)  # 打开分享页并截图，会截4张图。分别是：home.png,photo_page.png,
        bs.join_stting_page(key)  # 打开设置页
        bs.join_photo_edit(key)  # 打开打开图片编辑页
        bs.join_video_edit(key)  # 打开视频编辑页
        bs.join_photo_select_page(key)  # 打开图片选择页
        bs.join_video_select_page(key)  # 打开视频选择页
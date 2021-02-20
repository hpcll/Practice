import uiautomator2 as u2
from time import sleep


# 手机的IP
d = u2.connect('32caf2b1')
# 启动App
d.app_start("com.video.editor.filto")
sleep(1)
#打开设置
d(resourceId="com.video.editor.filto:id/iv_splash_setting").click()
sleep(1)
# 点击首页视频选择入口
d(resourceId="com.video.editor.filto:id/imageView4").click()
#点击首页图片选择入口
d(resourceId="com.video.editor.filto:id/imageView5").click()
#点击首页 订阅入口
d(resourceId="com.video.editor.filto:id/iv_sub_splash").click()
#选择图片
d.xpath('//*[@resource-id="com.video.editor.filto:id/rl_media"]/android.view.ViewGroup[2]').click()
#选择视频
d.xpath('//*[@resource-id="com.video.editor.filto:id/rl_media"]/android.view.ViewGroup[2]').click()
#点击视频编辑页中的特效
d.xpath('//*[@resource-id="com.video.editor.filto:id/tl_media_tool_type"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
#编辑页面保存
d(resourceId="com.video.editor.filto:id/tv_edit_save")
#编辑页返回
d(resourceId="com.video.editor.filto:id/iv_edit_back")
#
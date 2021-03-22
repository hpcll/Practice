import uiautomator2 as u2
from time import sleep

# 手机的IP
d = u2.connect('867df495')
# 启动App
d.app_start("com.video.editor.filto")
sleep(1)


############  首页  ##############
#打开设置
d(resourceId="com.video.editor.filto:id/iv_splash_setting").click()
sleep(1)

# 点击首页视频选择入口
d(resourceId="com.video.editor.filto:id/imageView4").click()

#点击首页图片选择入口
d(resourceId="com.video.editor.filto:id/imageView5").click()

#点击首页 订阅入口
d(resourceId="com.video.editor.filto:id/iv_sub_splash").click()


#########  相册选择页   ############
#选择图片或者视频
d.xpath('//*[@resource-id="com.video.editor.filto:id/rl_media"]/android.view.ViewGroup[2]').click()
sleep(1)

########## 编辑页  ################
#点击视频编辑页中的剪辑
d.xpath('//*[@resource-id="com.video.editor.filto:id/tl_media_tool_type"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
##点击编辑页中的X
d(resourceId="com.video.editor.filto:id/iv_clip_cancel").click()
##点击编辑页中的✅
d(resourceId="com.video.editor.filto:id/iv_clip_confirm").click()


#点击视频编辑页中的特效
d.xpath('//*[@resource-id="com.video.editor.filto:id/tl_media_tool_type"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()

#点击视频编辑页的画布
d.xpath('//*[@resource-id="com.video.editor.filto:id/tl_media_tool_type"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
##画布中的比例
d(resourceId="com.video.editor.filto:id/tv_title_ratio").click()#比例
###
d(resourceId="com.video.editor.filto:id/tv_ratio", text="16:9").click()#text后面填写对应的比例
##画布中背景切换
d(resourceId="com.video.editor.filto:id/tv_title_bg").click()#背景
###
d.xpath('//*[@resource-id="com.video.editor.filto:id/rl_bg"]/android.widget.FrameLayout[5]/android.view.View[1]').click()#FrameLayout[5]  5代表第五个背景色

#去水印
d(resourceId="com.video.editor.filto:id/tv_water_mark").click()
##关闭去水印弹框
d(resourceId="com.video.editor.filto:id/iv_water_mark_cancel").click()
###点击加入pro
d.xpath('//android.view.ViewGroup/android.widget.FrameLayout[1]').click()
###点击恢复购买
d(resourceId="com.video.editor.filto:id/tv_water_mark_restore").click()


#编辑页面保存
d(resourceId="com.video.editor.filto:id/tv_edit_save").click()
#编辑页返回
d(resourceId="com.video.editor.filto:id/iv_edit_back")


########## 语言切换页 ################
#点击选择语言
d(resourceId="com.video.editor.filto:id/spinner_language").click()
#点击语言
d(resourceId="android:id/text1", text="默认")#text后面直接切换相应的语言
#点击应用
d(resourceId="com.video.editor.filto:id/btn_setting_apply").click()
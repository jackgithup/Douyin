#coding:utf8
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

"""
from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

dev = connect_device('Android://<adbhost[localhost]>:<adbport[5037]>/<serialno>')
poco = AndroidUiautomationPoco(dev)
"""

class Douyin(object):
    def __init__(self):
        pass
        self.wait_time = 5
        

    def huawei(self):
        try:
            device_2 = connect_device('android:T7G0215804000411')
            poco = AndroidUiautomationPoco(device=device_2, use_airtest_input=True, screenshot_each_action=False)
            # poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

            for i in range(1,1000):
                print(f'第{i}次滑动！')
                poco.swipe([0.5, 0.8], [0.5, 0.2])
                time.sleep(self.wait_time)
                # 判断说是不是广告
                try:
                    #a7l
                    wenan = poco(name="com.ss.android.ugc.aweme:id/a7l").get_text()
                    if '[t]' in wenan:
                        print('this is a ad!')
                        continue
                    # ad_text = poco(name="com.ss.android.ugc.aweme:id/buf").get_text()
                    # print(f'ad_text:{ad_text}')
                    # if '查看详情' in ad_text:
                    #     print('this is a ad!')
                    #     continue
                except:
                    print('this not is a ad!')
                # with open('ad.txt','w') as f:
                #     f.write(ad_text)
                # 点击进入个人中心
                # 获取主播昵称
                text = poco(name="com.ss.android.ugc.aweme:id/title").get_text()
                self.write_file('users_name.txt',text)
                poco(name="com.ss.android.ugc.aweme:id/title").click()
                time.sleep(self.wait_time)

                # 进入商品橱窗
                try:
                    goods_text = poco(text="商品橱窗").get_text()
                    print(f'goods_text：{goods_text}')
                    if goods_text:
                        # poco(text="商品橱窗").click()
                        poco(name="com.ss.android.ugc.aweme:id/cl5").click()
                        # 返回
                        poco(name="com.ss.android.ugc.aweme:id/k4").click()
                except:
                    print('not hove goods!')
                # 返回
                try:
                    # poco(name="com.ss.android.ugc.aweme:id/kc").click()
                    poco(name="com.ss.android.ugc.aweme:id/k4").click()
                    time.sleep(self.wait_time)
                except:
                    # poco(name="com.ss.android.ugc.aweme:id/ww").click()
                    poco(name="com.ss.android.ugc.aweme:id/wf").click()
                    time.sleep(self.wait_time)

                # 点击进入音乐
                try:
                    # poco(name="com.ss.android.ugc.aweme:id/c3k").click()
                    poco(name="com.ss.android.ugc.aweme:id/c1o").click()
                    time.sleep(self.wait_time)
                    # poco(name="com.ss.android.ugc.aweme:id/kc").click()
                    poco(name="com.ss.android.ugc.aweme:id/k4").click()
                    time.sleep(self.wait_time)
                except:
                    #央视新闻
                    print('this music is not useful!')
            return True
            # 获取视频页面内容
            # text = poco(name="com.ss.android.ugc.aweme:id/a87").get_text()
            # self.write_file('users_name.txt',text)
        except:
            return False

        # with open('douyin_swip.txt', 'a', errors='ignore') as f:
        #     f.write(text + '\n')
        #     f.flush()
        # poco(name="com.ss.android.ugc.aweme:id/agx").set_text(username)
        # time.sleep(5)
        # poco(name="com.ss.android.ugc.aweme:id/e_v").click([0.1,0.9])
        # poco(name="android.widget.ImageView").click()
        # nicheng = poco(name="com.ss.android.ugc.aweme:id/c4i").get_text()
        # print(f'nicheng:{nicheng}')
        # douyinhao = poco(name="com.ss.android.ugc.aweme:id/eg0").get_text()
        # print(f'douyinhao:{douyinhao}')
        # try:
        #     company = poco(name="com.ss.android.ugc.aweme:id/ag0").get_text()
        # except:
        #     print('该抖音账户没有公司信息！')
        #     company = None
        # print(f'company:{company}')
        # sign = poco(name="com.ss.android.ugc.aweme:id/egs").get_text()
        # print(f'sign:{sign}')
        # huozan = poco(name="com.ss.android.ugc.aweme:id/a8v").get_text()
        # print(f'huozan:{huozan}')
        # guanzu = poco(name="com.ss.android.ugc.aweme:id/aon").get_text()
        # print(f'guanzu:{guanzu}')
        # fans = poco(name="com.ss.android.ugc.aweme:id/aoi").get_text()
        # print(f'fans:{fans}')
        # dict1 = {
        #     'nicheng': nicheng,
        #     'douyinhao': douyinhao,
        #     'company': company,
        #     'sign': sign,
        #     'huozan': huozan,
        #     'guanzu': guanzu,
        #     'fans': fans,
        # }
        # print(f'dict1:{dict1}')
        # with open('test4.txt', 'a', errors='ignore') as f:
        #     f.write(str(dict1) + '\n')
        #     f.flush()
        # write_file(dict1)
        # poco(name="com.ss.android.ugc.aweme:id/ka").click()
        # poco(name="com.ss.android.ugc.aweme:id/pr").click()
        # poco(name="com.ss.android.ugc.aweme:id/agx").click()
        # poco(name="com.ss.android.ugc.aweme:id/agx").set_text('我与大白')
        # time.sleep(5)
        # poco(name="com.ss.android.ugc.aweme:id/e_v").click()
        # poco(name="android.widget.ImageView").click()
        # nicheng = poco(name="com.ss.android.ugc.aweme:id/c4i").get_text()
        # print(f'nicheng:{nicheng}')
        # douyinhao = poco(name="com.ss.android.ugc.aweme:id/eg0").get_text()
        # print(f'douyinhao:{douyinhao}')
        # try:
        #     company = poco(name="com.ss.android.ugc.aweme:id/ag0").get_text()
        # except:
        #     print('该抖音账户没有公司信息！')
        #     company = None
        # print(f'company:{company}')
        # # sign = poco(name="com.ss.android.ugc.aweme:id/egs").get_text()
        # # print(f'sign:{sign}')
        # huozan = poco(name="com.ss.android.ugc.aweme:id/a8v").get_text()
        # print(f'huozan:{huozan}')
        # guanzu = poco(name="com.ss.android.ugc.aweme:id/aon").get_text()
        # print(f'guanzu:{guanzu}')
        # fans = poco(name="com.ss.android.ugc.aweme:id/aoi").get_text()
        # print(f'fans:{fans}')
        # dict1 = {
        #     'nicheng': nicheng,
        #     'douyinhao': douyinhao,
        #     'company': company,
        #     # 'sign': sign,
        #     'huozan': huozan,
        #     'guanzu': guanzu,
        #     'fans': fans,
        # }
        # print(f'dict1:{dict1}')
        # with open('test4.txt', 'a', errors='ignore') as f:
        #     f.write(str(dict1) + '\n')
        #     f.flush()

    def write_file(self,filename,dict1):
        with open(filename, 'a', errors='ignore') as f:
            f.write(str(dict1) + '\n')
            f.flush()

    def start1(self):
        pass
        if self.huawei():
            pass
        else:
            self.huawei()


if __name__ == '__main__':
    Douyin().huawei()
    # poco = AndroidUiautomationpoco(use_airtest_input=True, screenshot_each_action=False)
    # poco(name="com.ss.android.ugc.aweme:id/b8r").click()
    # poco(name="com.ss.android.ugc.aweme:id/agx").click()
    # usernames = ['周大侠', '小小画家', '我与大白']
    # for username in usernames:
    #     print(username)
    #     douyin(username)
    # for i in range(5):
    #     print(f'第{i}次刷新抖音！')

        # poco(text="首页").click()
        # poco(name="com.ss.android.ugc.aweme:id/dhr").click()
        # time.sleep(wait_time)


#点击进入个人中心的url
#https://aweme-eagle.snssdk.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAAVqble4cNrTStlcpe3oBpm43O7tMkaIBlcJSEV5-6ZlM&address_book_access=2&retry_type=no_retry&iid=91823970275&device_id=37162856753&ac=wifi&channel=huawei_1&aid=1128&app_name=aweme&version_code=860&version_name=8.6.0&device_platform=android&ssmix=a&device_type=HUAWEI+GRA-UL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0&uuid=866696027819133&openudid=c39a97a0a010126c&manifest_version_code=860&resolution=1080*1812&dpi=480&update_version_code=8602&_rticket=1573442098453&ts=1573442094&app_type=normal
# 个人页面的所有视频信息
# https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=0&sec_user_id=MS4wLjABAAAAVqble4cNrTStlcpe3oBpm43O7tMkaIBlcJSEV5-6ZlM&count=20&retry_type=no_retry&iid=91823970275&device_id=37162856753&ac=wifi&channel=huawei_1&aid=1128&app_name=aweme&version_code=860&version_name=8.6.0&device_platform=android&ssmix=a&device_type=HUAWEI+GRA-UL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0&uuid=866696027819133&openudid=c39a97a0a010126c&manifest_version_code=860&resolution=1080*1812&dpi=480&update_version_code=8602&_rticket=1573442098457&ts=1573442094&app_type=normal

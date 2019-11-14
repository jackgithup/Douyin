
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

wait_time = 0.5
def douyin(username):
    # poco(name="com.ss.android.ugc.aweme:id/agx").set_text(username)
    # poco(name="com.ss.android.ugc.aweme:id/ah7").set_text(username)
    # time.sleep(wait_time)
    # poco(name="com.ss.android.ugc.aweme:id/e_v").click()
    # poco(name="com.ss.android.ugc.aweme:id/ebd").click()  # 点击搜索到的第一个用户
    # time.sleep(wait_time)
    # poco(name="android.widget.ImageView").click()
    # poco(name="com.ss.android.ugc.aweme:id/ecv").click()  # 点击进入用户个人主页
    # time.sleep(wait_time)
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
    # poco(name="com.ss.android.ugc.aweme:id/kc").click()
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
    poco(name="com.ss.android.ugc.aweme:id/ah7").set_text(username)
    time.sleep(wait_time)
    poco(name="com.ss.android.ugc.aweme:id/ebd").click()  # 选择匹配到的第一个用户
    time.sleep(wait_time)
    poco(name="com.ss.android.ugc.aweme:id/ecv").click()  # 进入用户主页
    time.sleep(wait_time)
    poco(desc="返回").click()  # 返回
    time.sleep(wait_time)
    poco(name="com.ss.android.ugc.aweme:id/pw").click()  # X

def write_file(dict1):
    with open('test4.txt', 'a', errors='ignore') as f:
        f.write(str(dict1) + '\n')
        f.flush()


if __name__ == '__main__':
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # poco(name="com.ss.android.ugc.aweme:id/b8r").click()
    poco(desc="搜索").click()
    time.sleep(wait_time)
    # poco(name="com.ss.android.ugc.aweme:id/agx").click()
    usernames = ['周大侠', '小小画家', '我与大白']
    for username in usernames:
        print(username)
        douyin(username)
#八零老男人

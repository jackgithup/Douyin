# coding:utf8
import mitmproxy.http
import json
import pymongo
import re

true = 'true'
flalse = 'false'
null = 'null'

"""
mitmproxy增加二次代理
"""

class Counter:
    def __init__(self):
        pass
        # conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        # conn = pymongo.MongoClient("mongodb://120.92.122.11:27017/")
        # print('connect mongodb success!')
        # self.db = conn['appdata4']
        # print('create database success!')
        # db.authenticate('appdata_dev','LubanDev!2019AppdataDev')#, mechanism='SCRAM-SHA-1')
        # self.db.authenticate('appdata_dev', 'LubanDev!2019AppdataDev')
        # print('user renzheng success!')
        import pymysql as pymysql
        import io
        import sys
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
        self.db = pymysql.connect(host='120.92.76.67', port=63778, user='appdata', passwd='LubanDev!Appdata2019',
                             db='appdata1', charset='utf8')
        self.cursor = self.db.cursor()
        print('connect mysql success!')

    def request(self, flow: mitmproxy.http.HTTPFlow):
        print("开始修改ip")
        proxy = ("223.247.138.64", 16819)
        # mitmweb -p 8080 -s  mitmproy_getdata.py
        # mitmweb --mode upstream:http://59.57.241.102:15276 -s mitmproy_getdata.py
        # mitmweb --mode upstream:http://223.247.138.64:16819 --upstream-auth lijiabo:uvkjbzjz -s  mitmproy_getdata.py
        # 这里配置二级代理的ip地址和端口
        if flow.live:
            print("设置代理")
            flow.live.change_upstream_proxy_server(proxy)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        url1 = flow.request.url
        # cookies = dict(flow.request.cookies)
        # text = flow.response.get_text()
        # dict1 = {'url':url1,'cookies':cookies,'text':text}
        # print(dict1)
        # with open(cookie_mitmproxy,'a',errors='ignore') as f:
        #     f.write(str(dict1)+'\n')
        # print(url1)
        # print(cookies)
        # print('*' * 100)

        # 用户中心
        #https://aweme.snssdk.com/aweme/v1/user/
        #https://api-eagle.amemv.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAASldeksZ0YuV95V1nlJ_Ioo5Fh3E86dWLfBC1XUo8aL4&address_book_access=2&retry_type=no_retry&iid=92231024152&device_id=37162856753&ac=wifi&channel=tengxun_new&aid=1128&app_name=aweme&version_code=840&version_name=8.4.0&device_platform=android&ssmix=a&device_type=HUAWEI+GRA-UL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0&uuid=866696027819133&openudid=c39a97a0a010126c&manifest_version_code=840&resolution=1080*1812&dpi=480&update_version_code=8402&_rticket=1573644756771&ts=1573644756&app_type=normal
        if 'https://aweme-eagle.snssdk.com/aweme/v1/user/' in url1 or 'https://aweme.snssdk.com/aweme/v1/user/' in url1 or 'https://api-eagle.amemv.com/aweme/v1/user/' in  url1:
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text,strict=False)
            # print(json_data)
            # douyinhao = json_data['user']['short_id'] #unique_id
            # if douyinhao == '0':
            #     douyinhao = json_data['user']['unique_id']  # unique_id
            # print(f'douyinhao:{douyinhao}')
            # uid = json_data['user']['uid']
            # print(f'uid:{uid}')
            # print('*'*100)
            dict1 = {
                # 'douyinhao':douyinhao,
                # 'uid':uid,
                'url':url1,
                'headers':eval(str(headers)[7:]),
                'cookies':cookies,
            }
            print(dict1)
            dict1.update(json_data)
            for item in dict1['headers']:
                # print(item)
                if b'X-Gorgon' in item[0]:
                    # print(str(item[1],'utf8'))
                    x_gorgon = str(item[1],'utf8')
                if b'X-Khronos' in item[0]:
                    # print(str(item[1],'utf8'))
                    x_khronos = str(item[1],'utf8')
            # with open('json_data.txt','w',errors='ignore') as f:
            #     f.write(str(json_data))
            # self.storage_data('douyin_users',dict1)
            # print(url1)
            # print(x_gorgon)
            # print(x_khronos)
            # print(json_data)
            self.insert_mysql_user_table(url1, x_gorgon, x_khronos, json_data)

        # 用户中心下的所有视频
        #https://aweme.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&sec_user_id=MS4wLjABAAAA3b35RLwebzR7wztES6UqnqvbwdMuOeGcI-C2IJOIvdQ&count=20&retry_type=no_retry&iid=91823970275&device_id=37162856753&ac=wifi&channel=huawei_1&aid=1128&app_name=aweme&version_code=860&version_name=8.6.0&device_platform=android&ssmix=a&device_type=HUAWEI+GRA-UL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0&uuid=866696027819133&openudid=c39a97a0a010126c&manifest_version_code=860&resolution=1080*1812&dpi=480&update_version_code=8602&_rticket=1573468519606&ts=1573468514&app_type=normal
        if 'https://api.amemv.com/aweme/v1/aweme/post/' in url1 or 'https://aweme.snssdk.com/aweme/v1/aweme/post/' in url1:
            #https://api.amemv.com/aweme/v1/aweme/post/
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text, strict=False)
            # douyinhao = json_data['aweme_list'][0]['author']['short_id']  # unique_id
            # if douyinhao == '0':
            #     douyinhao = json_data['aweme_list'][0]['author']['unique_id']  # unique_id
            # print(f'douyinhao:{douyinhao}')
            # uid = json_data['aweme_list'][0]['author']['uid']
            # print(f'uid:{uid}')
            # print('*' * 100)
            dict1 = {
                # 'douyinhao':douyinhao,
                # 'uid':uid,
                'url': url1,
                'headers': eval(str(headers)[7:]),
                'cookies': cookies,
            }
            dict1.update(json_data)
            # with open('video.txt', 'a', errors='ignore') as f:
            #     f.write(str(dict1) + '\n')
            # self.storage_data('douyin_users_videos',dict1)
            # print('*' * 100)
            self.insert_mysql_aweme_table('', '', '', json_data)

        # 商品橱窗-获取商品信息
        # https://aweme.snssdk.com/aweme/v1/promotion/user/promotion/list/?count=20&cursor=0&user_id=111520113131&column_id=0&sort=0&sec_user_id=MS4wLjABAAAA71BrvQ5hDRBrjF4rDT0r4iHhUugItRBl4RAxR-B59Ik&os_api=23&device_type=HUAWEI%20GRA-UL00&device_platform=android&ssmix=a&iid=92231024152&manifest_version_code=840&dpi=480&uuid=866696027819133&version_code=840&app_name=aweme&version_name=8.4.0&ts=1573552715&openudid=c39a97a0a010126c&device_id=37162856753&resolution=1080*1812&os_version=6.0&language=zh&device_brand=HUAWEI&app_type=normal&ac=wifi&update_version_code=8402&aid=1128&channel=tengxun_new&_rticket=1573552715937
        # if 'https://aweme.snssdk.com/aweme/v1/promotion/user/promotion/list/' in url1:
        #     cookies = dict(flow.request.cookies)
        #     headers = flow.request.headers
        #     text = flow.response.get_text()
        #     json_data = json.loads(text, strict=False)
        #     # goods_list = json_data['promotions']
        #     # for item in goods_list:
        #     #     keys = item.keys()
        #     #     if 'toutiao' in keys:
        #     #         detail_url = item['detail_url']
        #     #         detail_list = detail_url.split("&")
        #     #         for item2 in detail_list:
        #     #             if 'origin_id' in item2:
        #     #                 print(item2)
        #     #                 uid = re.findall(r"origin_id=(.*?)_", item2)[0]
        #     #                 print(uid)
        #     #                 print(f'uid:{uid}')
        #     #                 print('*' * 100)
        #     dict1 = {
        #         # 'uid': uid,
        #         'url': url1,
        #         'headers': eval(str(headers)[7:]),
        #         'cookies': cookies,
        #     }
        #     dict1.update(json_data)
        #     # self.storage_data('douyin_goods', dict1)

        # 音乐中心
        #https://aweme.snssdk.com/aweme/v1/music/detail/?music_id=6705668538457148168&click_reason=0&os_api=23&device_type=HUAWEI%20GRA-UL00&device_platform=android&ssmix=a&iid=92231024152&manifest_version_code=840&dpi=480&uuid=866696027819133&version_code=840&app_name=aweme&version_name=8.4.0&ts=1573720552&openudid=c39a97a0a010126c&device_id=37162856753&resolution=1080*1812&os_version=6.0&language=zh&device_brand=HUAWEI&app_type=normal&ac=wifi&update_version_code=8402&aid=1128&channel=tengxun_new&_rticket=1573720554449
        if 'https://aweme.snssdk.com/aweme/v1/music/detail/' in url1:
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text, strict=False)
            # print(json_data)
            dict1 = {
                # 'uid': uid,
                'url': url1,
                'headers': eval(str(headers)[7:]),
                'cookies': cookies,
            }
            dict1.update(json_data)
            for item in dict1['headers']:
                # print(item)
                if b'X-Gorgon' in item[0]:
                    # print(str(item[1],'utf8'))
                    x_gorgon = str(item[1],'utf8')
                if b'X-Khronos' in item[0]:
                    # print(str(item[1],'utf8'))
                    x_khronos = str(item[1],'utf8')
            # self.storage_data('douyin_music', dict1)
            # print(url1)
            # print(x_gorgon)
            # print(x_khronos)
            # print(json_data)
            # print('*' * 100)
            self.insert_mysql_music_table(url1, x_gorgon, x_khronos, json_data)

        # 音乐中心下的所有视频
        #https://aweme.snssdk.com/aweme/v1/music/aweme/?music_id=6750989721029069576&cursor=0&count=20&type=0&os_api=23&device_type=HUAWEI%20GRA-UL00&device_platform=android&ssmix=a&iid=91823970275&manifest_version_code=860&dpi=480&uuid=866696027819133&version_code=860&app_name=aweme&version_name=8.6.0&ts=1573474027&openudid=c39a97a0a010126c&device_id=37162856753&resolution=1080*1812&os_version=6.0&language=zh&device_brand=HUAWEI&app_type=normal&ac=wifi&update_version_code=8602&aid=1128&channel=huawei_1&_rticket=1573474032088
        if 'https://aweme.snssdk.com/aweme/v1/music/aweme/' in url1:
            pass
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text, strict=False)
            # uid = json_data['aweme_list'][0]['author']['uid']
            # print(f'uid:{uid}')
            # print('*' * 100)
            dict1 = {
                # 'uid': uid,
                'url': url1,
                'headers': eval(str(headers)[7:]),
                'cookies': cookies,
            }
            dict1.update(json_data)
            # self.storage_data('douyin_music_videos', dict1)
            self.insert_mysql_aweme_table('', '', '', json_data)

    def storage_data(self,collection1,dict1):
        pass
        # self.collection = self.db[collection1]
        # self.collection.ensure_index('douyinhao', unique=True)
        # self.collection.ensure_index('uid', unique=True)
        # self.collection.insert_one(dict1)
        # print(f'{collection1} success insert one data!')
        # print('*'*100)
        # with open(f'{collection1}.txt','a',errors='ignore') as f:
        #     f.write(str(dict1)+'\n')
        #     f.flush()

    def insert_mysql_user_table(self,url, x_gorgon, x_khronos, json_data):
        # print(url, x_gorgon, x_khronos, json_data)
        # import pymysql as pymysql
        # import io
        # import sys
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
        # null = None
        # true = True
        # false = False
        # db = pymysql.connect(host='120.92.76.67', port=63778, user='appdata', passwd='LubanDev!Appdata2019',
        #                      db='appdata1', charset='utf8')
        # cursor = db.cursor()
        # print('connect mysql success!')
        item = {}
        item['uid'] = json_data['user']['uid']
        item['nickname'] = json_data['user']['nickname']
        item['unique_id_modify_time'] = json_data['user']['unique_id_modify_time']
        item['short_id'] = json_data['user']['short_id']
        item['unique_id'] = json_data['user']['unique_id']
        item['sec_uid'] = json_data['user']['sec_uid']
        item['country'] = json_data['user']['country']
        item['province'] = json_data['user']['province']
        try:
            item['location'] = json_data['user']['location']
        except:
            item['location'] = ''
        item['district'] = json_data['user']['district']
        item['following_count'] = json_data['user']['following_count']
        item['fans_count'] = json_data['user']['followers_detail'][0]['fans_count']
        item['aweme_count'] = json_data['user']['aweme_count']
        item['birthday'] = json_data['user']['birthday']
        item['signature'] = json_data['user']['signature']
        gender = json_data['user']['gender']
        if gender == 1:
            item['gender'] = '女'
        if gender == 2:
            item['gender'] = '男'
        try:
            item['school_name'] = json_data['user']['school_name']
        except:
            item['school_name'] = ''
        with_commerce_entry = json_data['user']['with_commerce_entry']
        if 'rue' in str(with_commerce_entry):
            item['with_commerce_entry'] = 1
        if 'alse' in str(with_commerce_entry):
            item['with_commerce_entry'] = 0
        item['avatar_thumb_uri'] = json_data['user']['avatar_thumb']['uri']
        item['avatar_thumb_url'] = json_data['user']['avatar_thumb']['url_list'][0]
        item['enterprise_verify_reason'] = json_data['user']['enterprise_verify_reason']
        try:
            item['offline_action'] = json_data['user']['commerce_info']['action']
        except:
            item['offline_action'] = ''
        item['url'] = url
        item['x_gorgon'] = x_gorgon
        item['x_khronos'] = x_khronos
        # print(item)
        sql = 'INSERT INTO user(uid,nickname,unique_id_modify_time,short_id,unique_id,sec_uid,country,province,location,district,following_count,fans_count,aweme_count,birthday,signature,gender,school_name,with_commerce_entry,avatar_thumb_uri,avatar_thumb_url,enterprise_verify_reason,offline_action,url,x_gorgon,x_khronos) ' \
              'values{}'.format(tuple(list(item.values())))
        # print('*' * 100)
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('insert_mysql_user_table success insert one data!')
        except:
            self.db.rollback()
            print('insert_mysql_user_table false insert one data!')
        # db.close()
        print('-' * 100)

    def insert_mysql_aweme_table(self,url, x_gorgon, x_khronos, json_data):
        aweme_list = json_data['aweme_list']
        for aweme in aweme_list:
            item = {}
            item['aweme_id'] = aweme['aweme_id']
            item['descs'] = aweme['desc']
            item['create_time'] = aweme['create_time']
            item['uid'] = aweme['author']['uid']
            item['short_id'] = aweme['author']['short_id']
            item['sec_uid'] = aweme['author']['sec_uid']
            item['nickname'] = aweme['author']['nickname']
            item['music_id'] = aweme['music']['id']
            item['comment_count'] = aweme['statistics']['comment_count']
            item['digg_count'] = aweme['statistics']['digg_count']
            item['download_count'] = aweme['statistics']['download_count']
            item['play_count'] = aweme['statistics']['play_count']
            item['share_count'] = aweme['statistics']['share_count']
            item['forward_count'] = aweme['statistics']['forward_count']
            item['lose_count'] = aweme['statistics']['lose_count']
            item['lose_comment_count'] = aweme['statistics']['lose_comment_count']
            item['rate'] = aweme['rate']
            item['is_delete'] = aweme['status']['is_delete']
            item['author_avatar_uri'] = aweme['author']['avatar_thumb']['uri']
            item['video_addr_uri'] = aweme['video']['play_addr']['uri']
            item['video_cover_url'] = aweme['video']['cover']['url_list'][0]
            item['video_dynamic_cover_url'] = aweme['video']['dynamic_cover']['url_list'][0]
            item['video_origin_cover_url'] = aweme['video']['origin_cover']['url_list'][0]
            item['url'] = url
            item['x_gorgon'] = x_gorgon
            item['x_khronos'] = x_khronos
            # print(item)
            sql = 'INSERT INTO aweme(aweme_id,descs,create_time,uid,short_id,sec_uid,nickname,music_id,comment_count,digg_count,download_count,play_count,share_count,forward_count,lose_count,lose_comment_count,rate,is_delete,author_avatar_uri,video_addr_uri,video_cover_url,video_dynamic_cover_url,video_origin_cover_url,url,x_gorgon,x_khronos) values{}'.format(
                tuple(list(item.values())))
            # print('*' * 100)
            # print(sql)
            try:
                self.cursor.execute(sql)
                self.db.commit()
                print('insert_mysql_aweme_table success insert one data!')
            except:
                self.db.rollback()
                print('insert_mysql_aweme_table false insert one data!')
            print('-' * 100)

    def insert_mysql_music_table(self,url='', x_gorgon='', x_khronos='', json_data=''):
        # import io
        # import sys
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
        music_info = json_data['music_info']
        item = {}
        item['music_id'] = music_info['id']
        item['author'] = music_info['author']
        item['sec_uid'] = music_info['sec_uid']
        item['title'] = music_info['title']  #
        item['shoot_duration'] = music_info['shoot_duration']  #
        item['duration'] = music_info['duration']  #
        item['cover_uri'] = music_info['cover_large']['uri']  #
        item['source_platform'] = music_info['source_platform']  #
        item['music_billboard_type'] = music_info['music_billboard_type']  #
        item['reason_type'] = music_info['reason_type']  #
        item['play_uri'] = music_info['play_url']['uri']  #
        item['owner_nickname'] = music_info['owner_nickname']  #
        item['user_count'] = music_info['user_count']  #
        item['url'] = url
        item['x_gorgon'] = x_gorgon  #
        item['x_khronos'] = x_khronos  #
        # insert_time
        # update_time
        # print(item)
        sql = 'INSERT INTO music(music_id,author,sec_uid,title,shoot_duration,duration,cover_uri,source_platform,music_billboard_type,reason_type,play_uri,owner_nickname,user_count,url,x_gorgon,x_khronos) values{}'.format(
            tuple(list(item.values())))
        # with open('music_table.txt','w') as f:
        #     f.write(str(sql))
        #     f.flush()
        # print('-' * 100)
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('insert_mysql_music_table success insert one data!')
        except:
            self.db.rollback()
            print('insert_mysql_music_table false insert one data!')
        print('-' * 100)


addons = [
    Counter()
]

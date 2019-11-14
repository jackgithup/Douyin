# coding:utf8
import mitmproxy.http
import json
import pymongo

flalse = False
null = None
class Counter:
    def __init__(self):
        pass
        conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        # conn = pymongo.MongoClient("mongodb://120.92.122.11:27017/")
        self.db = conn['appdata']
        print('connect mongodb success!')
        # db.authenticate('appdata_dev','LubanDev!2019AppdataDev')#, mechanism='SCRAM-SHA-1')
        # db.authenticate('appdata_dev', 'LubanDev!2019AppdataDev')
        # print('user renzheng success!')


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
        if 'https://aweme-eagle.snssdk.com/aweme/v1/user/' in url1:
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text,strict=False)
            dict1 = {
                'url':url1,
                'headers':eval(str(headers)[7:]),
                'cookies':cookies,
            }
            dict1.update(json_data)
            # with open('person.txt','a',errors='ignore') as f:
            #     f.write(str(dict1)+'\n')
            self.storage_data('douyin_users',dict1)
            print('*' * 100)
        if 'https://api.amemv.com/aweme/v1/aweme/post/' in url1:
            #https://api.amemv.com/aweme/v1/aweme/post/
            cookies = dict(flow.request.cookies)
            headers = flow.request.headers
            text = flow.response.get_text()
            json_data = json.loads(text, strict=False)
            dict1 = {
                'url': url1,
                'headers': eval(str(headers)[7:]),
                'cookies': cookies,
            }
            dict1.update(json_data)
            # with open('video.txt', 'a', errors='ignore') as f:
            #     f.write(str(dict1) + '\n')
            self.storage_data('douyin_videos',dict1)
            print('*' * 100)

    def storage_data(self,collection1,dict1):
        self.collection = self.db[collection1]
        # self.collection.ensure_index('douyinhao', unique=True)
        self.collection.insert_one(dict1)
        print('insert one data success!')

addons = [
    Counter()
]

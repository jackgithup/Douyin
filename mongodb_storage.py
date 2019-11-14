# coding:utf8
from pymongo import MongoClient
import pymongo

class Mongo1():
    def __init__(self):
        pass

    def insert_mongo(self):
        #myclient = pymongo.MongoClient('mongodb://root:123456@localhost:27017/')
        """
        线上 mongo
        host ：120.92.122.11
        port:27017

        database：appdata
        user：appdata_dev
        password:LubanDev!2019AppdataDev
        client = MongoClient("mongodb://host:port/")

        client.admin.authenticate("username","password",mechanism='SCRAM-SHA-1')（其中admin可以换成你的用户名能登录的库名）
        """
        # conn = MongoClient('127.0.0.1', 27017)
        # conn = MongoClient('mongodb://appdata_dev:LubanDev!2019AppdataDev@120.92.122.11:27017')
        # conn = MongoClient("mongodb://120.92.122.11:27017/")
        # conn = pymongo.MongoClient("mongodb://120.92.122.11:27017/")
        # db = conn['appdata']
        # print('connect mongodb success!')
        # db.authenticate('appdata_dev','LubanDev!2019AppdataDev')#, mechanism='SCRAM-SHA-1')
        # db.authenticate('appdata_dev','LubanDev!2019AppdataDev')
        # print('user renzheng success!')
        # db = conn['mydb']

        # print('database connect success!')
        # self.collection = db['users']
        # self.collection.ensure_index('douyinhao', unique=True)
        # print('collection connect success!')
        # myclient = pymongo.MongoClient("mongodb://120.92.122.11:27017/")
        # mydb = myclient["appdata"]
        # mydb.authenticate('appdata_dev', 'LubanDev!2019AppdataDev')


        dict1 = {'nicheng': '我与大白', 'douyinhao': '抖音号：345676425', 'company': None, 'sign': '感谢关注！', 'huozan': '2765.9w', 'guanzu': '65', 'fans': '251.2w'}
        dict2 = {'nicheng': '周大侠', 'douyinhao': '抖音号：107236383', 'company': None, 'sign': '美妆博主\n《大小姐升职记》等你追剧哟\nvx：zdx334\n周日到周四晚十点直播\n商务合作：cq35mm(注明来意)\n招募短视频艺人：jialejuyi88（卫星）', 'huozan': '522.6w', 'guanzu': '9', 'fans': '110.6w'}
        dict3 = {'nicheng': '小小画家', 'douyinhao': '抖音号：Cky668', 'company': '深圳市逸豪文化艺术有限公司', 'sign': '不求与人相比 ，但求超越自己', 'huozan': '1437.7w', 'guanzu': '107', 'fans': '140.0w'}

        # list1 = [dict1,dict2,dict3]
        # self.collection.insert_one(dict3)
        # print('insert one data success!')
        # self.collection.insert_many([dict1,dict2,dict3])
        # print('insert many datas success!')

    def select1(self):
        pass
        conn = MongoClient('127.0.0.1', 27017)
        db = conn['appdata4']
        print('connect mongodb success!')
        collection_name = 'douyin_music'
        collection = db[collection_name]
        print('connect collection success!')
        length = len(collection.find())
        print(length)
        # for x in collection.find():
        #     try:
        #         print(x)
        #         with open(f'{collection_name}.txt','a',errors='ignore') as f:
        #             f.write(str(x)+'\n')
        #             f.flush()
        #     except:
        #         pass

    def start1(self):
        pass
        # self.insert1()
        self.select1()


if __name__ == '__main__':
    mongo1 = Mongo1().start1()

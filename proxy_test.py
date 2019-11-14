# coding:utf8
# 本地公网：101.254.138.194
# ['223.247.138.64']
# ['223.247.138.64']
# 华为手机ip:10.240.8.112
# 电脑ip:10.240.6.245
# 首先确认代理的类型 是http还是https的来判断proxie的取值
#mitmweb --mode upstream:http://114.240.101.242:5672 -s server.py
import requests
from lxml import etree
"""
代理：
223.247.138.64
http端口：	16819

用户名：lijiabo
密码：uvkjbzjz
"""
proxy_dict = {
    # "http": "http://lijiabo:uvkjbzjz@223.247.138.64:16819/",
    # "https": "http://lijiabo:uvkjbzjz@223.247.138.64:16819/"
    "http": "http://115.202.34.217:18542/",
    "https": "http://115.202.34.217:18542/",
}

respons = requests.get('http://ip.filefab.com/index.php', proxies=proxy_dict)
doc = etree.HTML(respons.text)
print(doc.xpath('.//h1[@id="ipd"]/span/text()'))


# -*- coding: utf-8 -*-
# @Time : 2020-10-27 18:30 
# @Author : shen
# @File : test_jiaowu.py 
# @Software: PyCharm
import requests
from lxml import etree
import chaojiying
import chaojiying


if __name__ =="__main__":
    #登录的网址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    test_url = "https://so.gushiwen.cn/user/login.aspx"
    deng_url = "https://so.gushiwen.cn/user/login.aspx?from="
    #   //*[@id="imgCode"]/@src/
    response = requests.get(url=deng_url,headers=headers).text
    tree = etree.HTML(response)
    picture = tree.xpath('//*[@id="imgCode"]/@src')[0]
    ate = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
    tor = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    pic_url = "https://so.gushiwen.org/"+picture
    pic = requests.get(url=pic_url,headers=headers).content
    pic_name = '.'+picture+'.jpg'
    with open(pic_name,'wb') as fp:
        fp.write(pic)
        print(pic_name)

    pic_content = chaojiying.out_get(pic_name,1004)
    print(pic_content)
    data = {
        '__VIEWSTATE': ate,
        '__VIEWSTATEGENERATOR': tor,
        'from':'',
        'email': '15310665564',
        'pwd': '082730',
        'code': pic_content,
        'denglu': '登录'
    }

    response  = requests.post(url=test_url,data=data,headers=headers)
    print(response.status_code)
    with open('test.html','wb') as fp:
        fp.write(response.text.encode('utf-8'))

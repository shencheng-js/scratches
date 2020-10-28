# -*- coding: utf-8 -*-
# @Time : 2020-10-27 12:18 
# @Author : shen
# @File : get_resume.py 
# @Software: PyCharm


#先获取这些简历的下载链接，统一进行下载
import requests
from lxml import etree
import os
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    first_url = "http://sc.chinaz.com/jianli/free_"
    # fp = open("E:\grasp")
    for i in range(5,30):
        print(i)
        if i==1:
            url = 'http://sc.chinaz.com/jianli/free.html'
        else:
            url=first_url+str(i)+".html"
        apple = requests.get(url=url,headers=headers)
        response = apple.text
        apple.close()
        # print(response)
        tree = etree.HTML(response)
        li_list = tree.xpath('//div[@id="container"]/div/a/@href')

        for li in li_list:

            li_apple = requests.get(url=li,headers=headers)
            li_apple.encoding='utf-8'
            response = li_apple.text
            # print(response)
            tree = etree.HTML(response)


            try:
                jianli_name = tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
                jianli_url = tree.xpath('//div[@class="clearfix mt20 downlist"]//li[1]/a/@href')[0]
                # jianli_name = jianli_name.encode('iso-8859-1').decode('gbk')

                # print(jianli_name)
                data = requests.get(url=jianli_url, headers=headers).content
                path = r'E:\\grasp\\' + jianli_name + '.rar'
                with open(path, 'wb') as fp:
                    fp.write(data)
                    print(jianli_name + "下载成功")
            except:
                print("somthing happen")
# -*- coding: utf-8 -*-
# @Time : 2020-10-26 9:57 
# @Author : shen
# @File : pic_down.py 
# @Software: PyCharm

#爬取图片
import requests
from lxml import etree
import os
if __name__ == "__main__":
    base_url = "http://pic.netbian.com/4kmeinv/index_"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')

    for i in range(2,100):
        url = base_url+str(i)+".html"
        response = requests.get(url=url, headers=headers)
        # response.encoding = 'gbk'  这里其实就可以解决乱码了
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            img_url = "http://pic.netbian.com/" + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + ".jpg"
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            # print(img_name,img_url)
            # 请求图片进行持久化存储
            img_data = requests.get(url=img_url, headers=headers).content
            img_path = r'E:\\picture\\' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, "下载成功")

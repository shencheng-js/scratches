import requests
from lxml import etree

if __name__ =="__main__":
    url = "https://cq.58.com/ershoufang/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    #数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    # print(li_list)
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
import requests
import json
import xlwt
from time import sleep

requests.adapters.DEFAULT_RETRIES = 5
def getdata(start):
    # s = requests.session()
    # s.keep_alive = False

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    id_list = []
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    for i in range(1,3):
        data = {
            'on': 'true',
            'page': i,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json();

        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        # sleep(1)
    # print(id_list)
    # print(len(id_list))

    # 开始获取真正需要的data
    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    all_data_list = []

    for id in id_list:
        data = {
            'id': id
        }
        detail = requests.post(url=post_url, data=data, headers=headers).json()
        # sleep(1)
        # print(detail)
        all_data_list.append(detail)
        # sleep(1)
    return all_data_list
# fp = open('alldataa.xlsx','w',encoding='utf-8')
# json.dump(all_data_list,fp,ensure_ascii=False)
# print("over!!!")
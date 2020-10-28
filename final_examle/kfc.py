import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

city = input('输入城市：')
data = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': '1',
    'pageSize': '40'
}
response = requests.post(url, data=data, headers=headers).json()
for i in response['Table1']:
    store = i['storeName']
    address = i['addressDetail']
    print('store:' + store, 'address:' + address + '\n')
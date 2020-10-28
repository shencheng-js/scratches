from bs4 import BeautifulSoup
import requests

url = "https://home.firefoxchina.cn/"
response = requests.get(url=url)
response.encoding = response.apparent_encoding
# print(response.text)
response.close()
soup = BeautifulSoup(response.text,'html.parser')

print(soup.meta)


# list = soup.find_all('div')
# for i in list:
#     print(i)
#     print("==================")
#
# import requests
# url = 'https://www.dygod.net/html/tv/hytv/'
# req = requests.get(url)
# req.encoding = req.apparent_encoding
# print(req.text)
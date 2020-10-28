import requests
import re
import os
findpicLink = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
url = "https://www.qiushibaike.com/imgrank/page/2/";
if not os.path.exists('./qiutu'):
    os.mkdir('./qiutu')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
img_data = requests.get(url=url,headers=headers).text
img_list = re.findall(findpicLink,img_data,re.S)
print(len(img_list))
for src in img_list:
    src = 'https:'+src
    img = requests.get(url=src,headers=headers).content
    img_name = src.split('/')[-1]
    img_path = './qiutu/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img)
        print("保存"+img_name)
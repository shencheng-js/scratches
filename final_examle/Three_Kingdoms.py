import requests
from bs4 import BeautifulSoup


fp = open('../temp/sanguo.txt', 'w', encoding='utf-8')
url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(page_text,'lxml')
li_list = soup.select('.book-mulu >ul >li ')
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com'+li.a['href']
    #解析章节内容
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #解析出详情页内容
    detail_soup = BeautifulSoup(detail_page_text,'lxml')
    div_tag = detail_soup.find('div',class_='chapter_content')
    content = div_tag.text
    fp.write(title+':'+content+'\n')
    print(title+"爬取成功")
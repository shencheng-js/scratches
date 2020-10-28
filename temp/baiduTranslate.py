import requests
#有点问题，这里获得的json是另一部分
#后续改进
url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en";
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
word = input("请输入需要翻译的词汇")

data = {
    'from': 'zh',
    'to': 'en',
    'query': word,
    'simple_means_flag': '3',
    'sign': '797211.575786',
    'token': '8af20e04e150fdadaea9c94b16b4eafb',
    'domain': 'common'
}

response = requests.post(url=url,data=data,headers=headers).json()

for i in response['data']:
    print(i)
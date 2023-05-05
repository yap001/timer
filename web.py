import requests

url = "https://www.google.com" # 你想要爬取的网页URL
response = requests.get(url) # 发送HTTP GET请求

if response.status_code == requests.codes.ok: # 如果请求成功
    print(response.text) # 输出网页内容

import requests
import re
from bs4 import BeautifulSoup as bs 
def get_html(url):
    try:
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        # 发送请求
        response = requests.get(url, headers=headers)
        # 返回结果
        response.encoding="utf-8"
        html=response.text
        # sp=bs(html,"html.parser")
        # print(html)
        # filter_content=sp.find_all("div",id="sina_keyword_ad_area2")
        # count=0
        # for i in filter_content:
        c=re.findall(r'[\u4e00-\u9fa5]+',str(html))
        #     # print(count+1,c)
        return "".join(c)
    except:
        return "ERROR"
url="http://blog.sina.com.cn/s/blog_4a015e940102zalj.html?tj=hist"
c=get_html(url)
print(c)
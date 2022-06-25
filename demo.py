#coding=utf-8
import tkinter as tk
import requests
import jieba
import jieba.analyse
import math
from bs4 import BeautifulSoup as bs
import re
filtter={"新浪":0,"广告":0,"的":0,"黑体":0,"楷体":0}
filtter1=["新浪","广告"]
# def get_html(url):
#     import requests
#     try:
#         # 设置请求头
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
#         }
#         # 发送请求
#         response = requests.get(url, headers=headers)
#         # 返回结果
#         return response.content.decode('utf-8')
#     except:
#         return "ERROR"
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
        sp=bs(html,"html.parser")
        # print(html)
        filter_content=sp.find_all("div",id="sina_keyword_ad_area2")
        ans=""
        for i in filter_content:
            # print(i)
            c=re.findall(r'[\u4e00-\u9fa5]+',str(i))
        return "".join(c)
    except:
        return "ERROR"
# 解析源代码的中文字符串
# def get_chinese(html):
#     import re
#     chinese = re.findall(r'[\u4e00-\u9fa5]+', html)
#     # 换行返回
#     return ''.join(chinese)
# def get_article(url):
#     h=get_html(url)
#     if h!="ERROR":
#         return get_chinese(h)
#     else:
#         return 0
def get_tf(article):
    list=jieba.lcut(article,cut_all="True")
    list2=jieba.analyse.extract_tags(article,withWeight=True)
    list1=[]
    for i in list2:
        if i[0] not in filtter1:
            list1.append(i[0])
    dic={}
    for word in list:
        dic[word]=list.count(word)
    dic.update(filtter)
    print(dic,list1)
    return dic,list1
def get_simiar(dic1,dic2):
    dic={}
    dic.update(dic1)
    dic.update(dic2)
    upnum=0
    for i in dic:
        if dic1.get(i) and dic2.get(i):
            upnum+=dic1[i]*dic2[i]
        else:
            upnum+=0
    downnum1=0
    downnum2=0
    for i in dic1:
        downnum1+=dic1[i]*dic1[i]
    for i in dic2:
        downnum2+=dic2[i]*dic2[i]
    return upnum/(math.sqrt(downnum1)*math.sqrt(downnum2))
def show():
    # print("start")
    url1=input1.get()
    url2=input2.get()
    # print(url1,url2)
    article1=get_html(url1)
    article2=get_html(url2)
    tf1,list1=get_tf(article1)
    # print(tf1)    
    tf2,list2=get_tf(article2)
    c=get_simiar(tf1,tf2)  
    tk.Label(root,text="余弦相似度："+str(c),font=5).grid(row=3,column=1)
    tt1.delete(1.0, "end")
    tt2.delete(1.0, "end")
    tt1.insert(1.0,list1)
    tt2.insert(1.0,list2)
    # tk.Text(root
    # tk.Label(root,text="URl1高频词："+str(list1),font=1).grid(row=4)
    # tk.Label(root,text="URl2高频词："+str(list2),font=1).grid(row=5)
    with open("demo.txt","w",encoding="utf-8") as f:
        f.write("文章1\n"+article1+"\n")    
        f.write("文章2\n"+article2+"\n")
        f.write("tf1\n"+str(tf1)+"\n")    
        f.write("tf2\n"+str(tf2)+"\n")
        f.write("【相似度】\n"+str(c)) 
if __name__=="__main__":
    root=tk.Tk()
    root.title("信息内容安全课程设计")
    root.geometry("800x300")
    tk.Label(root,text="URL1: ",padx=10,pady=10,font=5).grid(row=0)
    tk.Label(root,text="URL2: ",padx=10,font=5).grid(row=1)
    input1=tk.Entry(root,width=60,font=5)
    input1.grid(row=0,column=1,)
    input2=tk.Entry(root,width=60,font=5)
    input2.grid(row=1,column=1)
    tk.Button(root,text="计算",width=7,height=2,font=4,bg="gray",fg="purple",command=show).grid(row=1,column=2,padx=30)
    # http://blog.sina.com.cn/s/blog_4a015e940102zalj.html?tj=hist
    # http://blog.sina.com.cn/s/blog_49d5822c0102z3tw.html?tj=hist
    tt1=tk.Text(root,width=60,height=2,font=5)
    tt1.insert(1.0,"URL1关键词")
    tt1.grid(row=4,column=1)
    tt2=tk.Text(root,width=60,height=2,font=5)
    tt2.insert(1.0,"URL2关键词")
    tt2.grid(row=5,column=1)
    root.mainloop()

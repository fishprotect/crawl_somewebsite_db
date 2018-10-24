import openpyxl
import requests
from bs4 import BeautifulSoup
import re
import random
import time
from tools.random_sleep import random_sleep_time

'''
######生成随机睡眠数
'''

'''
######从网页中提取网页的body内容
######主要使用requests库
'''
def get_url(url,header):
    try:
        random_sleep_time()
        con = requests.get(url,headers=header,timeout=30)
        con.raise_for_status()
       # con.encoding = con.apparent_encoding
        return con.text
    except:
        return ""
'''
######解析网页body的内容，并且从里面提取需要的信息
######主要使用BeautifulSoup库
'''
def parse_con(con,moive):
    con         = BeautifulSoup(con,"lxml")
    #电影名
    try:
        title       = con.find("span",attrs={"property":"v:itemreviewed"}).text
    except:
        title       = "不详"
    try:
        director    = con.find("a",attrs={"rel":"v:directedBy"}).text
    except:
        director    ="不详"

    #电影详情
    try:
        content     = con.find("span",attrs={"property":"v:summary"}).text.strip()
    except:
        content = "不详"
    #演员
    try:
        start       = con.find_all("a",attrs={"rel":"v:starring"})
        star = ""
        for i in start:
            star = star+i.text+"； "
    except:
        star = "不详"

    #电影上映时间
    try:
        init        = con.find("span",attrs={"property":"v:initialReleaseDate"}).text
    except:
        init        ="不详"

    #电影时长
    try:
        runtime     = con.find("span",attrs={"property":"v:runtime"}).text
    except:
        runtime     = "不详"
    moive={"title":title,'director':director,"star":star,"init":init,"runtime":runtime,"content":content}
    return moive





'''
######主函数，

'''
def xlsx_to_txt():
    #添加头部信息，简单的模拟浏览器
    agent = "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0"
    header = {'User-Agent':agent}

    nums = 1   ###表示电影排名

    wb = openpyxl.load_workbook("doubanTOP250.xlsx")
    ws = wb.active
    moive = {}
    for i in range(2,252):
        url = str(ws['C'+str(i)].value)
        con = get_url(url,header)
        if con==" ":
            print("error")
        else:
            moive = parse_con(con,moive)
            #文件名如果没有创建成功，则所有的事情都白做。下面的错误处理就是为了保证文件名不会出错
            try:
                with open(str(nums)+moive["title"]+".txt",'a',errors='ignore') as f:
                    f.write("电影名：\n     "+moive["title"]+"\n \n")
                    f.write("导  演：\n    "+moive["director"]+"\n \n")
                    f.write("演  员：\n    "+moive["star"]+"\n \n")
                    f.write("上映时间：\n    "+moive["init"]+"\n \n")
                    f.write("时  长：\n    "+moive["runtime"]+"\n \n")
                    f.write("详  情：\n    "+moive["content"]+"\n \n")
            except:
                moive["title"] = re.match("[\w\u2E80-\u9FFF]+",moive["title"]).group()
                with open(str(nums)+moive["title"]+".txt",'a',errors='ignore') as f:
                    f.write("电影名：\n     "+moive["title"]+"\n \n")
                    f.write("导  演：\n    "+moive["director"]+"\n \n")
                    f.write("演  员：\n    "+moive["star"]+"\n \n")
                    f.write("上映时间：\n    "+moive["init"]+"\n \n")
                    f.write("时  长：\n    "+moive["runtime"]+"\n \n")
                    f.write("详  情：\n    "+moive["content"]+"\n \n")
            print("完成：######"+moive['title']+"的TXT格式文件保存")
            

        nums=nums+1
    return ""


'''
######运行代码
'''



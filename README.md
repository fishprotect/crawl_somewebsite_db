# 爬取某网站的实验

#### 项目介绍
1. 本项目主要是用于学习实践，主要爬取排名top250的电影，主要用到的库，requests+BeautifulSoup+openpyxl
2. 随机延迟访问URL，
3. 添加headers，
4. (!!!!!!未完成)使用ip代理,从别的网站爬取ip代理,(!!!!!!未完成)

#### 安装教程

1. 安装requests      方法：pip install requests
2. beautifulsoup
3. lxml
4. openpyxl
安装方法均用pip。

#### 使用说明

1. 输出格式如附件，电影详细简介输出为xlsx文件，电影详情，每个电影保存一个TXT文件，文件名为该电影名。
2. top250_xlsx.py是将排名top250的电影爬取，并保存为xlsx文件，保存格式见附件xlsx格式的文件
3. xlsx_txt.py是将保存在top250.py代码爬取的xlsx格式文件中的电影链接提取出来，然后访问具体链接，爬取电影详情，并分别保存每个电影用其排名和电影名组成的TXT文件，保存格式见附件TXT格式的文件。

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 使用方法
1. 方法一：用Python3 直接运行/spider/main.py 文件
2. 方法二：直接双击 win上可运行的.exe格式的文件夹 里面的 mian_mian.exe文件

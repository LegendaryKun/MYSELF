#在凡科建站上创建网页添加学号，然后读取学号
'''
当在网页上修改学号时，可能改变网页的HTML导致获取学号信息错误
，这时可以把当前文本删除，然后新建文本重新添加学号。
'''

import requests
from bs4 import BeautifulSoup

GetUsers_url = 'https://bs17911042.icoc.bz/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}

html = requests.get(GetUsers_url,headers = headers)
html = BeautifulSoup(html.text, 'html.parser')


soup = html.find('div',class_="fk-editor simpleText fk-editor-break-word ")
#print(soup)
#print(soup.text)

soup = soup.find_all('div')
#print(soup)

L = []
for i in soup:
           i = str(i)
           i = i.strip('</div>')
           L.append(i)
           
print(L)






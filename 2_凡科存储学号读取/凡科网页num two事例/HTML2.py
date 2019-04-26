#在凡科建站上创建网页添加学号，然后读取学号
'''
当在网页上修改学号时，可能改变网页的HTML导致获取学号信息错误
，这时可以把当前文本删除，然后新建文本重新添加学号。
'''

import requests
from bs4 import BeautifulSoup

#GetUsers_url = 'https://bs17911042.icoc.bz/'
GetUsers_url = 'https://bs17911042-1.icoc.bz/'
html = requests.get(GetUsers_url)
html = BeautifulSoup(html.text, 'html.parser')


soup = html.find_all('div',class_="fk-editor simpleText fk-editor-break-word ")[-1]
print(soup)
#print(soup.text)

soup = soup.find_all('div')

L = []
for i in soup:
           i = str(i)
           i = i.strip('</div>')
           L.append(i)
           
print(L)






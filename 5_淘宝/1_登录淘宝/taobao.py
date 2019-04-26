#Selinium 登录淘宝
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class taobao_infos:

    def __init__(self,url):
        self.url = 'https://login.taobao.com/member/login.jhtml'  #淘宝登录页面
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()  #这句我加进去的
        self.wait = WebDriverWait(self.browser, 10)

    #处理登陆信息
    def login(self):
        self.browser.get(self.url)
        sleep(6)
        self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click() #密码登录
        sleep(2)
        self.browser.find_element_by_xpath('//*[@class="weibo-login"]').click()    #微博登录
        sleep(3)
        self.browser.find_element_by_name('username').send_keys('17865570232')  
        sleep(5)
        self.browser.find_element_by_name('password').click() #这一步是我加上去的，我发现登录时模仿鼠标点击输入框，验证码才会显示
        sleep(3)
        self.browser.find_element_by_name('password').send_keys('wb1324')
        sleep(4)

        Vcode = input('请输入验证码：')
        self.browser.find_element_by_name('verifycode').send_keys(Vcode)
        sleep(4)

        
        self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()  #登录


url = 'https://login.taobao.com/member/login.jhtml'
a = taobao_infos(url)
a.login()

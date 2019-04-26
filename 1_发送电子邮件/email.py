import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


#——————————————————————————————————————
#发送邮件通知
def mail(subject, mail_user, content):
    ret = True
    # 163 smtp
    mail_host = "smtp.163.com"                #网易SMTP服务器

    account_sender = "legendarykun@163.com"   #发送方Email地址
    sender_password="HU1324"                  #授权码第三方发送需要授权码

    #mail_user = "344799672@qq.com"
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["胡哥", account_sender])  #第一个参数是发送人，第二个参数是发送人邮箱地址
        msg['To'] = formataddr([mail_user, mail_user])      #第一个参数是接收人，很多邮件服务商在显示邮件时
                                                            #，会把收件人名字自动替换为用户注册的名字，第二个参数是接收人邮箱地址
        msg['Subject'] = subject                            #邮件主题
        server = smtplib.SMTP(mail_host, 25)
        server.login(account_sender, sender_password)       #login()方法用来登录SMTP服务器
        server.sendmail(account_sender, [mail_user, ], msg.as_string())
        server.quit()                                       # 这句是关闭连接的意思
    except Exception:
        ret = False
    return ret



subject = '问候'
content = ' 你好，' + str('昆哥！')
ret = mail(subject=subject, mail_user='1324761070@qq.com', content=content)
  

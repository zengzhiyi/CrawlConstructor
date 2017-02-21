# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/21 15:03'
import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('the body of the email is here http://www.baiu.com 傻逼')
msg['Subject'] = 'python'
msg['From'] = 'swjtu_mooc@sina.com'
msg['To'] = '1694609389@qq.com'

username = 'swjtu_mooc@sina.com'
password = 'swjtu_mooc'

smtp = smtplib.SMTP()
smtp.connect('smtp.sina.com')
smtp.login(username, password)
smtp.send_message(msg)
smtp.quit()
print('done')

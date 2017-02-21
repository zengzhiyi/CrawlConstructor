# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/21 16:21'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = "swjtu_mooc@sina.com"
password = "swjtu_mooc"
receiver = "1694609389@qq.com"

# 如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "don't panic"
msg["From"] = username
msg["To"] = receiver

# ---这是文字部分---
part = MIMEText("乔装打扮，不择手段")
msg.attach(part)

# ---这是附件部分---
# xlsx类型附件
part = MIMEApplication(open('foo.xlsx', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
msg.attach(part)

# jpg类型附件
part = MIMEApplication(open('foo.jpg', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
msg.attach(part)

# pdf类型附件
part = MIMEApplication(open('foo.pdf', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
msg.attach(part)

# mp3类型附件
part = MIMEApplication(open('foo.mp3', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
msg.attach(part)

smtp = smtplib.SMTP("smtp.sina.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
smtp.login(username, password)  # 登陆服务器
smtp.sendmail(username, receiver, msg.as_string())  # 发送邮件
smtp.close()
print('done')
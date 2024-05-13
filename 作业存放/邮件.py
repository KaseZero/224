import smtplib
from email.mime.text import MIMEText
msg=MIMEText('fuck you','plain','utf-8')
msg['from']='483227716@qq.com'
msg['To']='483227716@qq.com'
msg['Subject']='测试报告主题'


smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('483227716@qq.com','tzhwmiiuajszbgja')
smtp.sendmail('483227716@qq.com','483227716@qq.com',msg.as_string())

smtp.quit()


#1、组装邮件正文
#2、组装邮件头
#3、连接smtp服务器并发送邮件
import smtplib#建立连接smtp服务器并发送邮件
from email.mime.text import MIMEText#导入包纯文本
#混合表单发送
from email.mime.multipart import MIMEMultipart
#1\组装邮件正文
msg=MIMEMultipart()#声明一个混合表单发送方式  混合格式消息体
body=MIMEText("python发送的邮件真好啊","plain","utf-8")#plain是纯文字html文件
msg.attach(body)#将正文添加到Msg对象中
#2\组装邮件头
# body["From"]="test_results@sina.com"
# body["To"]="hanruixia@dayima.com"#收件人
# body["subject"]="from python" #发送的主题是什么
msg["From"]="ivan-me@163.com"
msg["To"]="hanruixia@dayima.com"#收件人
msg["subject"]="from python" #发送的主题是什么
#4、附件
with open("../report/report.html","rb") as f:
    att_file=f.read()#读取文件
att=MIMEText(att_file,'base64','utf-8') #64w位的文件
att["Content_type"]="application/octet-stream"   #声明附件的内容格式，MIMEtext数据流格式
att["Content_Dispositiond"]="attachment;filename='report.html'"#附件描述信息filename是附件显示的文件名
msg.attach(att)#将附件添加到消息对象中
#3\连接smtp服务器并发送邮件
smtp=smtplib.SMTP_SSL("smtp.163.com")#smtplib库,xinlang youxiang
smtp.login("ivan-me@163.com","hanzhichao123")#登陆邮箱
smtp.sendmail("ivan-me@163.com",
              "hanruixia@dayima.com",
               #body.as_string()
               msg.as_string())

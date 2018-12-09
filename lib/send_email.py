import smtplib#建立连接smtp服务器并发送邮件
from email.mime.text import MIMEText#导入包纯文本
from email.mime.multipart import MIMEMultipart
from conf import config


def send_report():
    msg=MIMEMultipart()#声明一个混合表单发送方式  混合格式消息体
    body=MIMEText(config.body,"plain","utf-8")#plain是纯文字html文件
    msg.attach(body)#将正文添加到Msg对象中
    #2\组装邮件头
    msg["From"]=config.smtp_user
    msg["To"]=config.receiver
    msg["subject"]=config.subject
    #4、附件
    with open(config.report_file,"rb") as f:
        att_file=f.read()#读取文件
    att=MIMEText(att_file,'base64','utf-8') #64w位的文件
    att["Content_type"]="application/octet-stream"   #声明附件的内容格式，MIMEtext数据流格式
    att["Content_Dispositiond"]="attachment;filename='report.html'"#附件描述信息filename是附件显示的文件名
    msg.attach(att)#将附件添加到消息对象中
    #3\连接smtp服务器并发送邮件
    smtp=smtplib.SMTP_SSL(config.smtp_server)#smtplib库,xinlang youxiang
    smtp.login(config.smtp_user,config.smtp_password)#登陆邮箱
    smtp.sendmail(config.smtp_user,
                  config.receiver,
                   #body.as_string()
                   msg.as_string())

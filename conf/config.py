
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

#路径配置
#config_past=os.path.abspath(__file__)#__file__当前文件,os.path.abspath()绝对路径
import os
project_past=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print("绝对路径：",project_past)
#数据文件目录
data_path=os.path.join(project_past,'data')#连接方法用os.path.join#相对路径
data_path=os.path.join(project_past,'data','data.xlsx')#绝对路径
#print("data文件的绝对路径：",data_path)
#日志文件
log_file=os.path.join(project_past,'log','log.txt')
report_file=os.path.join(project_past,'report','report2.html')
#print("日志文件的绝对路径：",report_file)

# log配置
import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=data_path,
                    )

#邮件配置
smtp_server='smtp.163.com'
smtp_user='ivan-me@163.com'
smtp_password='hanzhichao123'
receiver='hanruixia@dayima.com' #收件人
subject='接口测试报告真好啊'#正文
body='hello word pass all\n 一下附件为测试报告，请查收' #附件

is_send=False#是否发送邮件

if  __name__ == "__main__":
    logging.info("hello, world")
    logging.info("中文日志")
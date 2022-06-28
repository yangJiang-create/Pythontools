# encoding: utf-8
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class sendmail():
    def __init__(self):
        pass
    def sendmail(self,Newsender,mail,data,imagepath = None):
        form_addr=Newsender[0]
        password=Newsender[1]
        mail =mail.split(',')    
        smtp_server='smtp.qq.com'
        msg=MIMEMultipart()                          #发送附件的方法定义为一个变量
        
        content=f'''
        现在是北京时间{time.strftime("%R")}<br>
        早上好，我是你的python助手<br>
        一起来关注今日要闻吧:<br>'''
        for text in data:
            content+=f'<p><a href="{text[1]}">{text[0]}</a></p>'
        
        msg.attach(MIMEText(content,'html', 'utf-8'))  #添加正文
        
        if imagepath != None:
            mime_images = '<p><img src="cid:imageid{0}" alt="imageid{0}"></p>'.format(1)#批量添加图片时需要修改值
            mime_img = MIMEImage(open(imagepath, 'rb').read(), _subtype='octet-stream')
            mime_img.add_header('Content-ID', 'imageid')
            msg.attach(mime_img)#上传图片至缓存空间
            mime_html = MIMEText('<html><body><p>{0}</p>{1}</body></html>'.format('', mime_images), 'html', 'utf-8')# 上传正文
            msg.attach(mime_html)# 添加附图至正文

        msg['From'] = Header(form_addr)
        msg['To']=','.join(mail)
        msg['Subject']=Header(f"{time.localtime(time.time()).tm_mon}月{time.localtime(time.time()).tm_mday}日热搜快递")
        server=smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        server.login(form_addr,password)
        server.sendmail(form_addr,mail,msg.as_string())
        server.quit()
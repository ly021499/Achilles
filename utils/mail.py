# @Time   : 2022/11/4 15:46
# @Author : LOUIE
# @Desc   : 邮件发送

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from utils import log
from smtplib import SMTP
import setting
import os


class EMail(object):

    def __init__(self):
        self.username = "username"
        self.password = "password"
        self.host = "host"
        self.content = "content"
        self.subject = "subject"
        self.receiver = "receiver"
        self.filename = "filename"
        self.mmp = MIMEMultipart()
        self.smtp = SMTP()

    def email_header(self):
        """
        定义邮件头部信息
        :return: None
        """
        self.mmp["From"] = self.username
        self.mmp["To"] = self.receiver
        self.mmp["subject"] = self.subject

    def email_attachment(self):
        """
        定义邮件附件
        :return: None
        """
        list_dir = os.listdir(setting.REPORT_DIR)
        # 根据文件的修改时间进行排序
        list_dir.sort(key=lambda x: os.path.getmtime(setting.REPORT_DIR + "\\" + x))
        # 构建文件路径，-1代表最新时间的文件
        att_file_path = os.path.join(setting.REPORT_DIR, list_dir[-1])
        att_file = MIMEApplication(open(att_file_path, 'rb').read())
        att_file.add_header('Content-Disposition', 'attachment', filename=self.filename)
        self.mmp.attach(att_file)

    def email_content(self):
        """
        定义邮件正文
        :return: None
        """
        content = MIMEText(self.content, _charset="utf-8")
        self.mmp.attach(content)

    def send_email(self):
        """
        发送邮件步骤：
        1.连接邮件服务器
        2.登录邮箱
        3.传入邮箱文本内容
        4.发送邮件
        5.关闭smtp连接
        :return:
        """

        # 调用方法添加各项信息
        self.email_header()
        self.email_content()
        self.email_attachment()

        try:
            self.smtp.connect(self.host)
            self.smtp.login(self.username, self.password)
            self.smtp.sendmail(self.username, self.receiver, self.mmp.as_string().encode())
            log.info("biubiubiu !!!~~~  导弹发射成功!@#$%  颤抖吧~~~  *&^%愚蠢的人类")
        except Exception as e:
            log.error(f"warning warning !!! ===> 导弹未进入指定发射轨道，赶紧抢救，否则你家要炸了啊~~~\n 错误信息：{e}")
        finally:
            self.smtp.quit()

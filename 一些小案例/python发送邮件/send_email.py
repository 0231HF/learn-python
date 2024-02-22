#!/usr/bin/python

import smtplib
import sys
from email.mime.text import MIMEText

mail_host = '********'
mail_user = ''
mail_auth = '********'
send_name = mail_user
recv_name = ''


def excute(to, title, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = send_name
    msg['To'] = recv_name
    msg['Subject'] = title
    server = smtplib.SMTP(mail_host, 25)
    server.sendmail(mail_user, to, msg.as_string())
    server.quit()


def send(recv_name, body):
    excute(recv_name, '测试-kerberos账号信息不匹配', body)


"""
/bin/python3.6 /root/send_email.py 接受人邮箱 邮件内容
"""
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python sned_email.py <recv_name> <send_data>")
        sys.exit(1)
    recv_name = sys.argv[1]
    body = sys.argv[2]
    send(recv_name, body)

# -*- coding: utf-8 -*-
# ID: kpuscript2021@gmail.com
# PW: 스크립트언어2021

import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def GetMail():
    #global value
    host = "smtp.gmail.com" # Gmail STMP  서버 주소.
    port = "587"

    # 보내는 사람의 메일 주소 / 받는 사람의 메일 주소
    senderAddr = "kpuscript2021@gmail.com"
    recipientAddr = "game2raaaang@kpu.ac.kr"

    # 제목, 내용, 보내는 사람 / 받는 사람
    msg = MIMEMultipart("multipart", "alternative")
    msg['Subject'] = "[한국마사회X한국산업기술대학교] 요청하신" + self.meet.get() + "에서 진행한 경기의" + " 정보를 보내드립니다."
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # HTML문서 생성
    html = """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """

    # html text로 변환
    part2 = MIMEText(html, 'html', _charset='UTF-8')
    # html msg에 붙히기
    msg.attach(part2)

    # 메일을 발송한다.
    s = smtplib.SMTP(host,port)
    s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("kpuscript2021@gmail.com","tmzmflqxmdjsdj2021")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()








































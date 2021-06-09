import telepot
from Horse import *

class TelegramBot:
    def __init__(self):
        self.bot = telepot.Bot(token='1751413623:AAGqoVnH_9OE9sccrNOi1ozES27uWb-xhD0')
        self.chat_id = 1860711556

    def DefaultMessage(self, meet, year, month, date, HorseInfoList):
        message = "[한국마사회X한국산업기술대학교] 요청하신 " + meet + "에서 "\
                            + year+ "년 " + month + "월 " + date + "일 진행한 경기의 정보를 보내드립니다.\n"
        
        for i in range(10):
            message +=  HorseInfoList[i].GetInfo(ORD) + '순위 말의 정보입니다\n'\
                        + '마명: ' + HorseInfoList[i].GetInfo(HR_NAME) \
                        + '\n마번: ' + HorseInfoList[i].GetInfo(HR_NO) \
                        + '\n국적: ' + HorseInfoList[i].GetInfo(NAME) \
                        + '\n나이: ' + HorseInfoList[i].GetInfo(AGE) \
                        + '\n성별: ' + HorseInfoList[i].GetInfo(SEX) \
                        + '\n마주명: ' + HorseInfoList[i].GetInfo(OW_NAME) \
                        + '\n마주번호: ' + HorseInfoList[i].GetInfo(OW_NO) \
                        + '\n순위: ' + HorseInfoList[i].GetInfo(ORD) \
                        + '\n경주기록: ' + HorseInfoList[i].GetInfo(RC_TIME)

        self.bot.sendMessage(chat_id=1860711556, text=message)
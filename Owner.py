# owName: 마주명, owNo: 마주번호
# ownerHorss: 현 보유 두수
# stDate: 입사 일자
# rcCntY: 최근 1년 총 출주 횟수
# ord1CntY: 최근 1년 1착 횟수
# ord2CntY: 최근 1년 2착 횟수
# ord3CntY: 최근 1년 3착 횟수
# chaksunY: 최근 1년 착순 상금

OWNER_NAME = 0
OWNER_NUM = 1
ST_DATE = 2
OW_RCCNTY = 3
OW_ORD1CNTY = 4
OW_ORD2CNTY = 5
OW_ORD3CNTY = 6
CHAKSUNY = 7

class Owner:
    def __init__(self):
        self.InfoList = [''] * 8
    
    def SetInfo(self, data, index):
        self.InfoList[index] = data
    
    def GetInfo(self, index):
        return self.InfoList[index]
    
    def GetInfoList(self):
        return self.InfoList
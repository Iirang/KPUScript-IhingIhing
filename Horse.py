# raceResult
# hrName: 마명, hrNo: 마번, name: 국적, age: 나이, sex: 성별, ord: 순위
# owName: 마주명, owNo: 마주번호
# rcTime: 경주기록

#raceHorseInfo
# birthday: 생년월일, rank: 등급
# faHrName: 부마명, faHrNo: 부마번
# moHrName: 모마명, moHrNo: 모마번
# rcCntT: 통산 총 출주 횟수
# ord1CntT: 통산 1착 횟수, ord2CntT: 통산 2착 횟수, ord3CntT: 통산 3착 횟수
# rcCntY: 최근 1년 출주 횟수
# ord1CntY: 최근 1년 1위 횟수, ord2CntY: 최근 1년 2위 횟수, ord3CntY: 최근 1년 3위 횟수
# chaksunT: 통산 수득 상금

HR_NAME = 0
HR_NO = 1
NAME = 2
AGE = 3
SEX = 4
ORD = 5
OW_NAME = 6
OW_NO = 7
RC_TIME = 8
BIRTHDAY = 9
RANK = 10
FAHR_NAME = 11
FAHR_NO = 12
MOHR_NAME = 13
MOHR_NO = 14
RCCNTT = 15
ORD1CNTT = 16
ORD2CNTT = 17
ORD3CNTT = 18
RCCNTY = 19
ORD1CNTY = 20 
ORD2CNTY = 21
ORD3CNTY = 22
CHAKSUNT = 23

class Horse:
    def __init__(self):
        self.InfoList = [''] * 24

    def SetInfo(self, data, index):
        self.InfoList[index] = data
    
    def GetInfo(self, index):
        return self.InfoList[index]

    def GetInfoList(self):
        return self.InfoList
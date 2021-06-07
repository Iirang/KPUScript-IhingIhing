# raceResult
# hrName: 마명, hrNo: 마번, name: 국적, age: 나이, sex: 성별, ord: 순위
# owName: 마주명, owNo: 마주번호

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
BIRTHDAY = 8
RANK = 9
FAHR_NAME = 10
FAHR_NO = 11
MOHR_NAME = 12
MOHR_NO = 13
RCCNTT = 14
ORD1CNTT = 15
ORD2CNTT = 16
ORD3CNTT = 17
RCCNTY = 18
ORD1CNTY = 19
ORD2CNTY = 20
ORD3CNTY = 21
CHAKSUNT = 22

class Horse:
    def __init__(self):
        pass

    def SetInfo(self, data, index):
        if index == 0:
            self.hrName = data
        elif index == 1:
            self.hrNo = data
        elif index == 2:
            self.name = data
        elif index == 3:
            self.age = data
        elif index == 4:
            self.sex = data
        elif index == 5:
            self.ord = data
        elif index == 6:
            self.owName = data
        elif index == 7:
            self.owNo = data
        elif index == 8:
            self.birthday = data
        elif index == 9:
            self.rank = data
        elif index == 10:
            self.faHrName = data
        elif index == 11:
            self.faHrNo = data
        elif index == 12:
            self.moHrName = data
        elif index == 13:
            self.moHrNo = data
        elif index == 14:
            self.rcCntT = data
        elif index == 15:
            self.ord1CntT = data
        elif index == 16:
            self.ord2CntT = data
        elif index == 17:
            self.ord3CntT = data
        elif index == 18:
            self.rcCntY = data
        elif index == 19:
            self.ord1CntY = data
        elif index == 20:
            self.ord2CntY = data
        elif index == 21:
            self.ord3CntY = data
        elif index == 22:
            self.chaksunT = data
    
    def GetInfo(self, index):
        if index == 0:
            return self.hrName
        elif index == 1:
            return self.hrNo
        elif index == 2:
            return self.name
        elif index == 3:
            return self.age
        elif index == 4:
            return self.sex
        elif index == 5:
            return self.ord
        elif index == 6:
            return self.owName
        elif index == 7:
            return self.owNo
        elif index == 8:
            return self.birthday
        elif index == 9:
            return self.rank
        elif index == 10:
            return self.faHrName
        elif index == 11:
            return self.faHrNo
        elif index == 12:
            return self.moHrName
        elif index == 13:
            return self.moHrNo
        elif index == 14:
            return self.rcCntT
        elif index == 15:
            return self.ord1CntT
        elif index == 16:
            return self.ord2CntT
        elif index == 17:
            return self.ord3CntT
        elif index == 18:
            return self.rcCntY
        elif index == 19:
            return self.ord1CntY
        elif index == 20:
            return self.ord2CntY
        elif index == 21:
            return self.ord3CntY
        elif index == 22:
            return self.chaksunT

    def printInfo(self):
        print(self.hrName, self.hrNo, self.name, self.age, self.sex, self.ord, self.owName, self.owNo)
        print(self.birthday, self.rank, self.faHrName, self.faHrNo, self.moHrName, self.moHrNo)
        print(self.rcCntT, self.ord1CntT, self.ord2CntT, self.ord3CntT)
        print(self.rcCntY, self.ord1CntY, self.ord2CntY, self.ord3CntY)
        print(self.chaksunT)
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

class Horse:
    def __init__(self):
        self.InfoList = []

    def SetRaceresultInfo(self, hrName, hrNo, name, age, sex, ord, owName, owNo):
        self.InfoList.extend(hrName, hrNo, name, age, sex, ord, owName, owNo)
    
    def SetRacehorseInfo(self, birthday, rank, faHrName, faHrNo, moHrName, moHrNo, rcCntT, ord1CntT, ord2CntT, ord3CntT, rcCntY, ord1CntY, ord2CntY, ord3CntY, chaksunT):
        self.InfoList.extend(birthday, rank, faHrName, faHrNo, moHrName, moHrNo, rcCntT, ord1CntT, ord2CntT, ord3CntT, rcCntY, ord1CntY, ord2CntY, ord3CntY, chaksunT)
# -*- coding: utf-8 -*-
import urllib.request
from xml.etree import ElementTree

ServiceKey = 'Jnx4DBhGQtUPd5DJUoi0WMJSBLPyJlHbmnhxHtz8XtFaGul%2FfaIKT%2BMULxP%2BaVRGFC7bYbca%2FoHde8dfxM%2BuHA%3D%3D'

class raceHorseInfo:
    def __init__(self):
        self.url = 'http://apis.data.go.kr/B551015/API8/raceHorseInfo'
        self.isError = False
    
    def setParam(self, hr_name, hr_no, meet):
        self.hr_name = hr_name
        self.hr_no = hr_no
        self.meet = meet
        
    def LoadXML(self):
        self.RacehorseinfoURL = self.url + '?serviceKey=' + ServiceKey + '&pageNo=1&numOfRows=1&hr_name=' + self.hr_name \
                            + '&hr_no=' + self.hr_no + '&meet=' + self.meet

        self.request = urllib.request.Request(self.RacehorseinfoURL)
        self.response = urllib.request.urlopen(self.request)
        self.rescode = self.response.getcode()

        if(self.rescode == 200):
            self.response_body = self.response.read()
            self.tree = ElementTree.fromstring(self.response_body)
            
        else:
            self.isError = True
            print('xml load fail')
    
    def LoadHorseInfo(self):
        # birthday, rank, faHrName, faHrNo, moHrName, moHrNo, rcCntT, ord1CntT, ord2CntT, ord3CntT, rcCntY, ord1CntY, ord2CntY, ord3CntY, chaksunT
        HorseInfo = []
        itemElements = self.tree.iter('item')
        for item in itemElements:
            birthday = item.findtext('birthday')
            rank = item.findtext('rank')
            faHrName = item.findtext('faHrName')
            faHrNo = item.findtext('faHrNo')
            moHrName = item.findtext('moHrName')
            moHrNo = item.findtext('moHrNo')
            rcCntT = item.findtext('rcCntT')
            ord1CntT = item.findtext('ord1CntT')
            ord2CntT = item.findtext('ord2CntT')
            ord3CntT = item.findtext('ord3CntT')
            rcCntY = item.findtext('rcCntY')
            ord1CntY = item.findtext('ord1CntY')
            ord2CntY = item.findtext('ord2CntY')
            ord3CntY = item.findtext('ord3CntY')
            chaksunT = item.findtext('chaksunT')

            HorseInfo.extend([birthday, rank, faHrName, faHrNo, moHrName, moHrNo, rcCntT, ord1CntT, ord2CntT, ord3CntT, rcCntY, ord1CntY, ord2CntY, ord3CntY, chaksunT])

        return HorseInfo
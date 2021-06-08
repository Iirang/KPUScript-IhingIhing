# -*- coding: utf-8 -*-
import urllib.request
from urllib.parse import quote
from xml.etree import ElementTree

# 임정균 111227
# &pageNo=1&numOfRows=10&meet=1&ow_name=%EC%9E%84%EC%A0%95%EA%B7%A0&ow_no=111227

ServiceKey = 'Jnx4DBhGQtUPd5DJUoi0WMJSBLPyJlHbmnhxHtz8XtFaGul%2FfaIKT%2BMULxP%2BaVRGFC7bYbca%2FoHde8dfxM%2BuHA%3D%3D'

class horseOwnerInfo:
    def __init__(self):
        self.url = 'http://apis.data.go.kr/B551015/API14/horseOwnerInfo'
        self.isError = False

    def setParam(self, meet, ow_name, ow_no):
        self.meet = meet
        self.ow_name = quote(ow_name)
        self.ow_no = ow_no
    
    def LoadXML(self):
        self.horseOwnerInfoURL = self.url + '?serviceKey=' + ServiceKey + '&pageNo=1&numOfRows=1&meet=' + self.meet + '&ow_name=' + self.ow_name + '&ow_no=' + self.ow_no

        self.request = urllib.request.Request(self.horseOwnerInfoURL)
        self.response = urllib.request.urlopen(self.request)
        self.rescode = self.response.getcode()

        if(self.rescode == 200):
            self.response_body = self.response.read()
            self.tree = ElementTree.fromstring(self.response_body)
        else:
            self.isError = True
            print('xml load fail')
        
        def LoadhorseOwnerInfo(self):
            OwnerInfo = []
            itemElements = self.tree.iter('item')
            for item in itemElements:
                owName = item.findtext('owName')
                owNo = item.findtext('owNo')
                ownerHorses = item.findtext('ownerHorses')
                stDate = item.findtext('stDate')
                rcCntY = item.findtext('rcCntY')
                ord1CntY = item.findtext('ord1CntY')
                ord2CntY = item.findtext('ord2CntY')
                ord3CntY = item.findtext('ord3CntY')
                chaksunY = item.findtext('chaksunY')

                OwnerInfo.extend([owName, owNo, ownerHorses, stDate, rcCntY, ord1CntY, ord2CntY, ord3CntY, chaksunY])
            
            return OwnerInfo

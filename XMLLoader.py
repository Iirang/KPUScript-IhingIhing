# -*- coding: utf-8 -*-
import urllib.request
from xml.etree import ElementTree

ServiceKey = 'Jnx4DBhGQtUPd5DJUoi0WMJSBLPyJlHbmnhxHtz8XtFaGul%2FfaIKT%2BMULxP%2BaVRGFC7bYbca%2FoHde8dfxM%2BuHA%3D%3D'

# Example Data
# examdate = '20210507'
# meet = '1'
# rc_date = '20210507'
# rc_month = '202105'
# rc_no = '1'
# rc_year = '2021'

class raceResult:
    def __init__(self):
        self.url = 'http://apis.data.go.kr/B551015/API4/raceResult'
        self.isError = False
    
    def getParam(self, examdate, meet, rc_date, rc_month, rc_no, rc_year):
        self.examdate = examdate
        self.meet = meet
        self.rc_date = rc_date
        self.rc_month = rc_month
        self.rc_no = rc_no
        self.rc_year = rc_year
    
    def LoadXML(self):
        self.RaceresultURL = self.url + '?serviceKey=' + ServiceKey + '&pageNo=1&numOfRows=10&examdate=' + self.examdate \
                             + '&meet=' + self.meet + '&rc_date=' + self.rc_date + '&rc_month=' + self.rc_month + '&rc_no=' + self.rc_no + '&rc_year=' + self.rc_year

        self.request = urllib.request.Request(self.RaceresultURL)
        self.response = urllib.request.urlopen(self.request)
        self.rescode = self.response.getcode()

        if(self.rescode == 200):
            self.response_body = self.response.read()
            self.tree = ElementTree.fromstring(self.response_body)
            print('xml load complete')
            
        else:
            self.isError = True
            print('xml load fail')
            #print("Error Code: "+ self.rescode)
        
    def setLabel(self): # 보여줄 것: 지역, 날짜, 날씨, 주로 상태(건조주로(1% ~ 5%) , 양호주로(6% ~ 9%), 다습주로(10% ~ 14%), 포화주로(15% ~ 19%), 불량주로(20% 이상))
        pass
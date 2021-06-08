from tkinter import *
import tkinter.ttk
from tkinter import font
from Horse import *
from Owner import *
from raceResult import *
from raceHorseInfo import *
from horseOwnerInfo import *
from Map import *
from gmail import *


class MainGUI():

    def Search(self):
        self.HorseInfoList.clear()
        self.HorseInfoList = [Horse() for _ in range(10)] # 말 정보 리스트

        self.OwnerInfoList.clear()
        self.OwnerInfoList = [Owner() for _ in range(10)] # 마주 정보 리스트

        if self.meet.get() == '서울':
            meet = '1'
        elif self.meet.get() == '제주':
            meet = '2'
        elif self.meet.get() == '부산' or self.meet.get() == '부산경남':
            meet = '3'
        
        month = self.month.get().rjust(2, '0')
        date = self.date.get().rjust(2, '0')
        examdate = self.year.get() + month + date
        rc_month = self.year.get() + month
        rc_no = self.rcNum.get()
        rc_year = self.year.get()

        self.raceResult.setParam(examdate, meet, examdate, rc_month, rc_no, rc_year)
        self.raceResult.LoadXML()
        self.OutputLabel['text'] = self.raceResult.setLabel()

        resultInfo = self.raceResult.LoadraceResultInfo()   # 9개

        for i in range(10):
            for j in range(9):
                self.HorseInfoList[i].SetInfo(resultInfo[i * 9 + j], j % 9)

        horseInfo = [['']*15]*10

        for i in range(10):
            name = self.HorseInfoList[i].GetInfo(HR_NAME)
            no = self.HorseInfoList[i].GetInfo(HR_NO)
            
            self.raceHorseInfo.setParam(name, no, meet)
            self.raceHorseInfo.LoadXML()
            horseInfo[i] = self.raceHorseInfo.LoadHorseInfo()   # 15개

        for i in range(10):
            for j in range(15):
                self.HorseInfoList[i].SetInfo(horseInfo[i][j], j % 15 + 9)
        
        ownerInfo = [['']*8]*10

        for i in range(10):
            name = self.HorseInfoList[i].GetInfo(OW_NAME)
            no = self.HorseInfoList[i].GetInfo(OW_NO)

            self.horseOwnerInfo.setParam(meet, name, no)
            self.horseOwnerInfo.LoadXML()
            ownerInfo[i] = self.horseOwnerInfo.LoadhorseOwnerInfo() # 9개

        for i in range(10):
            for j in range(9):
                self.OwnerInfoList[i].SetInfo(ownerInfo[i][j], j)

    def ShowMap(self):
        if self.meet.get() == '서울':
            Seoul()
        elif self.meet.get() == '제주':
            Jeju()
        elif self.meet.get() == '부산' or self.meet.get() == '부산경남':
            Busan()

    def SendMail(self):
        GetMail()
    
    def CurSelect(self, evt):   # evt를 사용하지 않더라도, tkinter에서 이벤트를 설명하는 객체를 호출하기 때문에 evt를 매개변수로 추가해야 한다.
        index = self.HorseListbox.index(self.HorseListbox.curselection())
        
        HorseInfoList = self.HorseInfoList[index].GetInfoList()
        OwnerInfoList = self.OwnerInfoList[index].GetInfoList()

        self.raceInfoLabel['text']  = '마명: ' + HorseInfoList[HR_NAME] + '\n마번: ' + HorseInfoList[HR_NO]\
                                    + '\n국적: ' + HorseInfoList[NAME] + '\n나이: ' + HorseInfoList[AGE]\
                                    + '\n성별: ' + HorseInfoList[SEX]\
                                    + '\n마주명: ' + HorseInfoList[OW_NAME] + '\n마주번호: ' + HorseInfoList[OW_NO]\
                                    + '\n순위: ' + HorseInfoList[ORD] + '\n경주기록: ' + HorseInfoList[RC_TIME]

        self.raceHorseInfoLabel['text'] = '생일: ' + HorseInfoList[BIRTHDAY] + '\n등급: ' + HorseInfoList[RANK]\
                                        + '\n부마명, 번: ' + HorseInfoList[FAHR_NAME] + ', ' + HorseInfoList[FAHR_NO]\
                                        + '\n모마명, 번: ' + HorseInfoList[MOHR_NAME] + ', ' + HorseInfoList[MOHR_NO]\
                                        + '\n통산 총 출주 횟수: ' + HorseInfoList[RCCNTT]\
                                        + '\n통산 1착 횟수: ' + HorseInfoList[ORD1CNTT]\
                                        + '\n통산 2착 횟수: ' + HorseInfoList[ORD2CNTT]\
                                        + '\n통산 3착 횟수: ' + HorseInfoList[ORD3CNTT]\
                                        + '\n최근 1년 출주 횟수: ' + HorseInfoList[RCCNTY]\
                                        + '\n최근 1년 1위 횟수: ' + HorseInfoList[ORD1CNTY]\
                                        + '\n최근 1년 2위 횟수: ' + HorseInfoList[ORD2CNTY]\
                                        + '\n최근 1년 3위 횟수: ' + HorseInfoList[ORD3CNTY]\
                                        + '\n통산 수득 상금: ' + HorseInfoList[CHAKSUNT]

        self.horseOwnerInfoLabel['text']    = '마주명: ' + OwnerInfoList[OWNER_NAME] + '\n마주번호: ' + OwnerInfoList[OWNER_NUM]\
                                            + '\n입사 일자: ' + OwnerInfoList[ST_DATE]\
                                            + '\n현 보유 두수: '+ OwnerInfoList[OWNERHORSES]\
                                            + '\n최근 1년 총 출주 횟수: ' + OwnerInfoList[OW_RCCNTY]\
                                            + '\n최근 1년 1착 횟수: ' + OwnerInfoList[OW_ORD1CNTY]\
                                            + '\n최근 1년 2착 횟수: ' + OwnerInfoList[OW_ORD2CNTY]\
                                            + '\n최근 1년 3착 횟수: ' + OwnerInfoList[OW_ORD3CNTY]\
                                            + '\n최근 1년 착순 상금: ' + OwnerInfoList[CHAKSUNY]                      

    def __init__(self):
        self.window = Tk()
        self.window.title("경마 정보 어플리케이션 - 이힝이힝")
        self.window.iconbitmap('Resource/Icon.ico') # 아이콘 추가
        self.window.geometry("800x600")
        self.window['bg'] = 'white'

        self.LogoImage = PhotoImage(file='Resource/Logo_Up_b.gif')
        self.font1 = font.Font(size=15, weight='bold', family='맑은 고딕')
        self.font2 = font.Font(size=10, weight='bold', family='맑은 고딕')

        LogoFrame = Frame(self.window, width=800, height=110, bg='white')
        LogoFrame.pack()
        Label(LogoFrame, image=self.LogoImage, height=110, bg='white').pack()

        self.SearchLabel = []   # 0: 지역, 1: 년도, 2: 월, 3: 일, 4: 경주 번호
        self.SearchEntry = [] 
        SearchFrame = Frame(self.window, bg='white')    # 입력받아야 할 것: 지역(1: 서울, 2: 제주, 3: 부산), 날짜(년, 월, 일), 경주 번호
                                                        # Entry 개수: 지역(1)+날짜(3)+경주 번호(1) = 5
        SearchFrame.pack()

        self.SearchLabel.append(Label(SearchFrame, text='지역', font=self.font1, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='년', font=self.font1, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='월', font=self.font1, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='일', font=self.font1, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='경주 번호', font=self.font1, bg='white'))

        self.meet = StringVar()     # 지역
        self.year = StringVar()     # 년도
        self.month = StringVar()    # 월
        self.date = StringVar()     # 일
        self.rcNum = StringVar()    # 경주 번호

        self.SearchEntry.append(Entry(SearchFrame, textvariable=self.meet, width=5, font=self.font1, justify=RIGHT))
        self.SearchEntry.append(Entry(SearchFrame, textvariable=self.year, width=5, font=self.font1, justify=RIGHT))
        self.SearchEntry.append(Entry(SearchFrame, textvariable=self.month, width=5, font=self.font1, justify=RIGHT))
        self.SearchEntry.append(Entry(SearchFrame, textvariable=self.date, width=5, font=self.font1, justify=RIGHT))
        self.SearchEntry.append(Entry(SearchFrame, textvariable=self.rcNum, width=5, font=self.font1, justify=RIGHT))

        for i in range(5):
            self.SearchEntry[i].pack(padx=(10, 0), side=LEFT)
            self.SearchLabel[i].pack(padx=(10, 0), side=LEFT)

        Button(SearchFrame, text='검색', command=self.Search, font=self.font1).pack(padx=(10, 0), side=LEFT)
        Button(SearchFrame, text='지도', command=self.ShowMap, font=self.font1).pack(padx=(10, 0), side=LEFT)  # TODO: text 없애고, 지도 이미지 추가

        OutputFrame = Frame(self.window, height=50, bg='white')    # 보여줄 것: 지역, 날짜, 날씨, 주로 상태(건조주로(1% ~ 5%) , 양호주로(6% ~ 9%), 다습주로(10% ~ 14%), 포화주로(15% ~ 19%), 불량주로(20% 이상))
        OutputFrame.pack()

        self.OutputLabel = Label(OutputFrame, text='\t\t검색 값을 입력하고 버튼을 눌러주세요.\t\t', font=self.font1, bg='white')
        self.OutputLabel.pack(side=LEFT)

        HorseFrame = Frame(self.window, bg='white')
        HorseFrame.pack()
        HorseScrollbar = Scrollbar(HorseFrame, orient=VERTICAL)
        self.HorseListbox = Listbox(HorseFrame, font= self.font1, height=8, selectmode=SINGLE)  # 선택하면 우측 Label에 정보 출력
        self.HorseListbox.pack(side=LEFT)
        HorseScrollbar.pack(side=LEFT, fill=Y)

        self.HorseListbox.config(yscrollcommand=HorseScrollbar.set)
        HorseScrollbar.config(command=self.HorseListbox.yview)
    
        for i in range(10):
            self.HorseListbox.insert(i, str(i+1)+'번 우승마')
        
        self.HorseListbox.bind('<<ListboxSelect>>', self.CurSelect) # 리스트에서 말을 선택하였을 때, self.CurSelect가 호출된다.

        self.HorseInfoNotebook = tkinter.ttk.Notebook(HorseFrame, width=220, height=220)
        self.HorseInfoNotebook.pack(padx=(10, 0), side=LEFT)

        self.raceInfoFrame = Frame(self.window, width=220, height=220, bg='white')
        self.raceHorseInfoFrame = Frame(self.window, width=220, height=220, bg='white')
        self.horseOwnerInfoFrame = Frame(self.window, width=220, height=220, bg='white')
        self.HorseInfoNotebook.add(self.raceInfoFrame, text='경주기록 정보')
        self.HorseInfoNotebook.add(self.raceHorseInfoFrame, text='경주마 상세정보')
        self.HorseInfoNotebook.add(self.horseOwnerInfoFrame, text='마주 상세정보')

        self.raceInfoLabel = Label(self.raceInfoFrame, bg='white', justify=LEFT, text='경기를 입력하고,\n좌측 리스트에서 말을 선택해주세요.', font=self.font2)
        self.raceInfoLabel.pack(anchor=W)

        self.raceHorseInfoLabel = Label(self.raceHorseInfoFrame, bg='white', justify=LEFT, text='경기를 입력하고,\n좌측 리스트에서 말을 선택해주세요.', font=self.font2)
        self.raceHorseInfoLabel.pack(anchor=W)

        self.horseOwnerInfoLabel = Label(self.horseOwnerInfoFrame, bg='white', justify=LEFT, text='경기를 입력하고,\n좌측 리스트에서 말을 선택해주세요.', font=self.font2)
        self.horseOwnerInfoLabel.pack(anchor=W)

        self.canvas = Canvas(HorseFrame, width=220, height=235, bg='white') # 그래프를 출력할 canvas
        self.canvas.pack(padx=(10, 0), side=LEFT)                           # TODO: 승률 비교 그래프 그리는 함수 추가

        ButtonFrame = Frame(self.window, bg='white')
        ButtonFrame.pack()
        Button(ButtonFrame, text='텔레그램', font=self.font1).pack(padx=(590, 0), side=LEFT) # TODO: 텔레그램 봇 연동
        Button(ButtonFrame, text='Gmail', command=self.SendMail, font=self.font1).pack(padx=(10, 0), side=LEFT) # TODO: Gmail 연동

        # 아래 칸 로고
        self.DownLogoImage = PhotoImage(file='Resource/Logo_Down_a.gif')
        DownLogoFrame = Frame(self.window, width=800, height=120, bg='white')
        DownLogoFrame.pack()
        Label(DownLogoFrame, image=self.DownLogoImage, height=120, bg='white').pack()

        self.HorseInfoList = [] # 말 정보 리스트
        self.OwnerInfoList = [] # 마주 정보 리스트

        self.raceResult = raceResult()  # 경주기록 정보 API
        self.raceHorseInfo = raceHorseInfo()  # 경주마 상세정보 API
        self.horseOwnerInfo = horseOwnerInfo() # 마주 상세정보 API

        self.window.mainloop()

MainGUI()
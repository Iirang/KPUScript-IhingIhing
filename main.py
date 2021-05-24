from tkinter import *
from tkinter import font

# 아이콘 생성을 위한 헤더, pyqt5를 패키징 해야한다.
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#TODO: 지도 버튼 위치 변경, 텔레그램 버튼, 메일 버튼, 하단 이미지 추가

# setWindowIcon을 위해선 (QWidget)이 필요하다.
class MainGUI():

    def Search(self):   # TODO: OpenAPI 연동하여 검색한 정보를 불러오는 기능 구현
        pass

    def ShowMap(self):  # TODO: 지도 연동
        pass

    def __init__(self):
        self.window = Tk()
        self.window.title("경마 정보 어플리케이션 - 이힝이힝")

        # 아이콘 불러오는 기능이라는데 왜 안불러 오는지는 잘 모르겠어서 우선 넣어볼께...
        # self.setWindowIcon(QIcon('Icon.png'))

        self.window.geometry("800x600")

        # TODO: LogoImage 수정
        self.LogoImage = PhotoImage(file='Resource/Logo_Up.gif')
        self.font = font.Font(size=15, weight='bold', family='맑은 고딕')

        LogoFrame = Frame(self.window, width=800, height=100)
        LogoFrame.pack()
        Label(LogoFrame, image=self.LogoImage, height=100).pack()

        self.SearchLabel = []   # 0: 지역, 1: 년도, 2: 월, 3: 일, 4: 경주 번호
        self.SearchEntry = [] 
        SearchFrame = Frame(self.window)    # 입력받아야 할 것: 지역(1: 서울, 2: 제주, 3: 부산), 날짜(년, 월, 일), 경주 번호
                                            # Entry 개수: 지역(1)+날짜(3)+경주 번호(1) = 5
        SearchFrame.pack()
        self.SearchLabel.append(Label(SearchFrame, text='지역    ', font=self.font))
        self.SearchLabel.append(Label(SearchFrame, text='년    ', font=self.font))
        self.SearchLabel.append(Label(SearchFrame, text='월    ', font=self.font))
        self.SearchLabel.append(Label(SearchFrame, text='일    ', font=self.font))
        self.SearchLabel.append(Label(SearchFrame, text='경주 번호\t   ', font=self.font))

        for i in range(5):
            self.SearchEntry.append(Entry(SearchFrame, width=5, font=self.font, justify=RIGHT))
            self.SearchEntry[i].pack(side=LEFT)
            self.SearchLabel[i].pack(side=LEFT)
        Button(SearchFrame, text='검색', command=self.Search, font=self.font).pack(side=LEFT)

        OutputFrame = Frame(self.window, height=50)    # 보여줄 것: 지역, 날짜, 날씨, 주로 상태(건조주로(1% ~ 5%) , 양호주로(6% ~ 9%), 다습주로(10% ~ 14%), 포화주로(15% ~ 19%), 불량주로(20% 이상))
        OutputFrame.pack()
        self.OutputLabel = Label(OutputFrame, text='\t\t검색 값을 입력하고 버튼을 눌러주세요.\t\t', font=self.font)
        self.OutputLabel.pack(side=LEFT)
        Button(OutputFrame, text='지도', command=self.ShowMap, font=self.font).pack(side=LEFT)  # TODO: text 없애고, 지도 이미지 추가

        HorseFrame = Frame(self.window)
        HorseFrame.pack()
        HorseScrollbar = Scrollbar(HorseFrame, orient=VERTICAL)
        self.HorseListbox = Listbox(HorseFrame, font= self.font, height=8)  # 선택하면 우측 Listbox에 정보 출력
        self.HorseListbox.pack(side=LEFT)
        HorseScrollbar.pack(side=LEFT, fill=Y)

        self.HorseListbox.config(yscrollcommand=HorseScrollbar.set)
        HorseScrollbar.config(command=self.HorseListbox.yview)
    
        for i in range(10):
            self.HorseListbox.insert(i, str(i+1)+'번 우승마')
        
        HorseInfoScrollbar = Scrollbar(HorseFrame, orient=VERTICAL)
        self.HorseInfoListbox = Listbox(HorseFrame, font=self.font, height=8)
        self.HorseInfoListbox.pack(padx=(10, 0), side=LEFT)
        HorseInfoScrollbar.pack(side=LEFT, fill=Y)

        self.HorseInfoListbox.config(yscrollcommand=HorseScrollbar.set)
        HorseInfoScrollbar.config(command=self.HorseInfoListbox.yview)

        self.canvas = Canvas(HorseFrame, width=220, height=235, bg='white') # 그래프를 출력할 canvas
        self.canvas.pack(padx=(10, 0), side=LEFT)                           # TODO: 승률 비교 그래프 그리는 함수 추가

        # 아래칸 로고
        self.DownLogoImage = PhotoImage(file='Resource/Logo_Down.gif')
        DownLogoFrame = Frame(self.window, width=800, height=120)
        DownLogoFrame.pack()
        Label(DownLogoFrame, image=self.DownLogoImage, height=120).pack()

        self.window.mainloop()


MainGUI()
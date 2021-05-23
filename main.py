from tkinter import *
from tkinter import font
from typing import ContextManager

class MainGUI:
    def Search(self):   # TODO: OpenAPI 연동하여 검색한 정보를 불러오는 기능 구현
        pass

    def ShowMap(self):  # TODO: 지도 연동
        pass

    def __init__(self):
        self.window = Tk()
        self.window.title("경마 정보 어플리케이션 - 이힝이힝")
        self.window.geometry("800x600")

        self.LogoImage = PhotoImage(file='Resource/KPU.gif')    # TODO: LogoImage 수정
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

        HorseListFrame = Frame(self.window)
        HorseListFrame.pack()
        HorseScrollbar = Scrollbar(HorseListFrame)
        self.HorseListBox = Listbox(HorseListFrame, font= self.font, height=5, yscrollcommand=HorseScrollbar.set)
        self.HorseListBox.pack(side=LEFT, anchor=NW)
        HorseScrollbar.pack(side=LEFT, anchor= NW, fill=Y)
        HorseScrollbar.config(command=self.HorseListBox.yview)

        for i in range(10):
            self.HorseListBox.insert(i, str(i+1)+'번 우승마')
        
        self.window.mainloop()

MainGUI()
from tkinter import *
from tkinter import font

#TODO: 지도 버튼 위치 변경, 텔레그램 버튼, 메일 버튼 추가

class MainGUI():

    def Search(self):   # TODO: OpenAPI 연동하여 검색한 정보를 불러오는 기능 구현
        pass

    def ShowMap(self):  # TODO: 지도 연동
        pass

    def __init__(self):
        self.window = Tk()
        self.window.title("경마 정보 어플리케이션 - 이힝이힝")
        self.window.iconbitmap('Resource/Icon.ico') # 아이콘 추가
        self.window.geometry("800x600")
        self.window['bg'] = 'white'

        self.LogoImage = PhotoImage(file='Resource/Logo_Up.gif')
        self.font = font.Font(size=15, weight='bold', family='맑은 고딕')

        LogoFrame = Frame(self.window, width=800, height=100, bg='white')
        LogoFrame.pack()
        Label(LogoFrame, image=self.LogoImage, height=100, bg='white').pack()

        self.SearchLabel = []   # 0: 지역, 1: 년도, 2: 월, 3: 일, 4: 경주 번호
        self.SearchEntry = [] 
        SearchFrame = Frame(self.window, bg='white')    # 입력받아야 할 것: 지역(1: 서울, 2: 제주, 3: 부산), 날짜(년, 월, 일), 경주 번호
                                                        # Entry 개수: 지역(1)+날짜(3)+경주 번호(1) = 5
        SearchFrame.pack()
        self.SearchLabel.append(Label(SearchFrame, text='지역', font=self.font, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='년', font=self.font, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='월', font=self.font, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='일', font=self.font, bg='white'))
        self.SearchLabel.append(Label(SearchFrame, text='경주 번호', font=self.font, bg='white'))

        for i in range(5):
            self.SearchEntry.append(Entry(SearchFrame, width=5, font=self.font, justify=RIGHT))
            self.SearchEntry[i].pack(padx=(10, 0), side=LEFT)
            self.SearchLabel[i].pack(padx=(10, 0), side=LEFT)
        Button(SearchFrame, text='검색', command=self.Search, font=self.font).pack(padx=(10, 0), side=LEFT)
        Button(SearchFrame, text='지도', command=self.ShowMap, font=self.font).pack(padx=(10, 0), side=LEFT)  # TODO: text 없애고, 지도 이미지 추가

        OutputFrame = Frame(self.window, height=50, bg='white')    # 보여줄 것: 지역, 날짜, 날씨, 주로 상태(건조주로(1% ~ 5%) , 양호주로(6% ~ 9%), 다습주로(10% ~ 14%), 포화주로(15% ~ 19%), 불량주로(20% 이상))
        OutputFrame.pack()
        self.OutputLabel = Label(OutputFrame, text='\t\t검색 값을 입력하고 버튼을 눌러주세요.\t\t', font=self.font, bg='white')
        self.OutputLabel.pack(side=LEFT)

        HorseFrame = Frame(self.window, bg='white')
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

        ButtonFrame = Frame(self.window, bg='white')
        ButtonFrame.pack()
        Button(ButtonFrame, text='텔레그램', font=self.font).pack(padx=(590, 0), side=LEFT) # TODO: 텔레그램 봇 연동
        Button(ButtonFrame, text='Gmail', font=self.font).pack(padx=(10, 0), side=LEFT) # TODO: Gmail 연동

        # 아래 칸 로고
        self.DownLogoImage = PhotoImage(file='Resource/Logo_Down.gif')
        DownLogoFrame = Frame(self.window, width=800, height=120, bg='white')
        DownLogoFrame.pack()
        Label(DownLogoFrame, image=self.DownLogoImage, height=120, bg='white').pack()

        self.window.mainloop()


MainGUI()
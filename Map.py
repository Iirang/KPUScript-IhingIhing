from tkinter import *
import folium
import webbrowser

def Seoul():
    # 렛츠런파크 서울점 위도,경도
    map_osm = folium.Map(location=[37.44550742218299, 127.01604695696804], zoom_start=15)

    #편의점
    folium.Marker([37.449042,127.013279], popup='CU 렛츠런파크럭키빌점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    folium.Marker([37.447807, 127.016736], popup='GS25 경마놀이터점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    folium.Marker([37.446496, 127.012892], popup='GS25 R서울구북2점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    #은행
    folium.Marker([37.44449957599277, 127.01235843084788], popup='NH농협은행 마사회지점', icon=folium.Icon(color='orange',icon='copyright-mark')).add_to(map_osm)
    #영역표시
    folium.Circle([37.445658605391834, 127.01526216286554], popup='렛츠런파크 서울점', radius=700).add_to(map_osm)

    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

def Busan():
    # 렛츠런파크 부산경남점 위도,경도
    map_osm = folium.Map(location=[35.15669337467454, 128.87656647475873], zoom_start=15)

    #편의점
    folium.Marker([35.15474842543499, 128.88065669204212], popup='CU 경마공원점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    folium.Marker([35.15624466168434, 128.8805818816516], popup='GS25 가락대로점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    #은행
    folium.Marker([35.152505328077126, 128.88218758240978], popup='경남은행 미음공단지점', icon=folium.Icon(color='orange',icon='copyright-mark')).add_to(map_osm)
    folium.Marker([35.15991625911274, 128.8805971945136], popup='농협은행 부산강서지점', icon=folium.Icon(color='orange',icon='copyright-mark')).add_to(map_osm)
    #영역표시
    folium.Circle([35.15560556718595, 128.87485173514398], popup='렛츠런파크 부산경남점', radius=800).add_to(map_osm)

    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

def Jeju():
    # 렛츠런파크 제주점 위도,경도
    map_osm = folium.Map(location=[33.40808389749586, 126.39896949341683], zoom_start=15)

    #편의점
    folium.Marker([33.4102966448231, 126.39883766393811], popup='GS25 엘리시안점', icon=folium.Icon(color='red',icon='shopping-cart')).add_to(map_osm)
    #은행
    folium.Marker([33.405986380271386, 126.40005879875261], popup='농협은행 제주경마공원출장소', icon=folium.Icon(color='orange',icon='copyright-mark')).add_to(map_osm)
    #영역표시
    folium.Circle([33.40749995214954, 126.4001873595549], popup='렛츠런파크 부산경남점', radius=850).add_to(map_osm)

    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')


window= Tk()
Button(window, text='렛츠런 파크 서울점', command=Seoul).pack()
Button(window, text='렛츠런 파크 부산경남점', command=Busan).pack()
Button(window, text='렛츠런 파크 제주', command=Jeju).pack()

window.mainloop()
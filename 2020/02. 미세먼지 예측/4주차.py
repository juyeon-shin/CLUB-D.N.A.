# -*- coding: utf-8 -*-
"""
미세먼지 4주차 서울
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df = pd.DataFrame()

#한글 폰트 지정
font_location = 'C:/Windows/Fonts/*.ttf'
font_name = fm.FontProperties(fname = font_location).get_name()
plt.rc('font', family='New Gulim')


'''
!pip install plotly
import plotly.express as px
dp = px.data.gapminder()
'''
#데이터 불러오기

Seoul_2019 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/Seoul_2019.xlsx')
train_2020 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/Seoul_2020.xlsx')

#결측값 확인
Seoul_2019.isnull().sum()

지역                0
망                 0
측정소코드             0
측정소명              0
측정일시              0
SO2           11913
CO            12642
O3            11143
NO2           13387
PM10          20433
PM25          17190
주소                0

#결측값 선형으로 채우기
Seoul_2019 = Seoul_2019.interpolate()
Seoul_2019.isnull().sum()

지역            0
망             0
측정소코드         0
측정소명          0
측정일시          0
SO2           0
CO            0
O3            0
NO2           0
PM10          0
PM25          0
주소            0
dtype: int64



#측정 일시를 월단위로 바꾸기
Seoul_2019['측정일시'] = Seoul_2019['측정일시'].astype('str')
Seoul_2019['날짜'] = Seoul_2019['측정일시'].str[:-2]
Seoul_2019['월'] = Seoul_2019['측정일시'].str[4:6]
Seoul_2019['시간'] = Seoul_2019['측정일시'].str[-2:]


#지역으로 분리하는 것
country_jungranggu = Seoul_2019['지역'] == '서울 중랑구'
jungranggu = Seoul_2019[country_jungranggu]

country_junggu = Seoul_2019['지역'] == '서울 중구'
junggu = Seoul_2019[country_junggu]

country_jongrogu = Seoul_2019['지역'] == '서울 종로구'
jongrogu = Seoul_2019[country_jongrogu]

country_enpyeonggu = Seoul_2019['지역'] == '서울 은평구'
enpyeonggu = Seoul_2019[country_enpyeonggu]

country_yongsangu = Seoul_2019['지역'] == '서울 용산구'
yongsangu = Seoul_2019[country_yongsangu]

country_yeongdungpogu = Seoul_2019['지역'] == '서울 영등포구'
yeongdungpogu = Seoul_2019[country_yeongdungpogu]

country_yangchengu = Seoul_2019['지역'] == '서울 양천구'
yangchengu = Seoul_2019[country_yangchengu]

country_songpagu = Seoul_2019['지역'] == '서울 송파구'
songpagu = Seoul_2019[country_songpagu]

country_sengbukgu = Seoul_2019['지역'] == '서울 성북구'
sengbukgu = Seoul_2019[country_sengbukgu]

country_sengdonggu = Seoul_2019['지역'] == '서울 성동구'
sengdonggu = Seoul_2019[country_sengdonggu]

country_seochogu = Seoul_2019['지역'] == '서울 서초구'
seochogu = Seoul_2019[country_seochogu]

country_seodeamungu = Seoul_2019['지역'] == '서울 서대문구'
seodeamungu = Seoul_2019[country_seodeamungu]

country_mapogu = Seoul_2019['지역'] == '서울 마포구'
mapogu = Seoul_2019[country_mapogu]

country_dongjackgu = Seoul_2019['지역'] == '서울 동작구'
dongjackgu = Seoul_2019[country_dongjackgu]

country_dongdeamungu = Seoul_2019['지역'] == '서울 동대문구'
dongdeamungu = Seoul_2019[country_dongdeamungu]

country_dobonggu = Seoul_2019['지역'] == '서울 도봉구'
dobonggu = Seoul_2019[country_dobonggu]

country_noonegu = Seoul_2019['지역'] == '서울 노원구'
noonegu = Seoul_2019[country_noonegu]

country_guomcheonggu = Seoul_2019['지역'] == '서울 금천구'
guomcheonggu = Seoul_2019[country_guomcheonggu]

country_gurogu = Seoul_2019['지역'] == '서울 구로구'
gurogu = Seoul_2019[country_gurogu]

country_gwangjingu = Seoul_2019['지역'] == '서울 광진구'
gwangjingu = Seoul_2019[country_gwangjingu]

country_gwanakgu = Seoul_2019['지역'] == '서울 관악구'
gwanakgu = Seoul_2019[country_gwanakgu]

country_gangseogu = Seoul_2019['지역'] == '서울 강서구'
gangseogu = Seoul_2019[country_gangseogu]

country_gangbukgu = Seoul_2019['지역'] == '서울 강북구'
gangbukgu = Seoul_2019[country_gangbukgu]

country_gangdonggu = Seoul_2019['지역'] == '서울 강동구'
gangdonggu = Seoul_2019[country_gangdonggu]

country_gangnamgu = Seoul_2019['지역'] == '서울 강남구'
gangnamgu = Seoul_2019[country_gangnamgu]



#전체 지역 평균
country_19 = Seoul_2019.groupby(['지역'], as_index=False).mean()

fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('지역 별 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_19,ax=axes[0])
axes[0].set_xticklabels(country_19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_19,ax=axes[1])
axes[1].set_xticklabels(country_19.지역.unique(),rotation=45, ha='right')


#지역 합치기 (서울 권역 참고)
#동북권 도봉 노원 강북 성북 동대문 중랑 성동 광진
country_en = pd.concat([dobonggu,noonegu,gangbukgu,sengbukgu,dongdeamungu,jungranggu,sengdonggu,gwangjingu], axis = 0)
country_en19 = country_en.groupby(['지역'], as_index=False).mean()

#동남권 서초 강남 송파 강동
country_es = pd.concat([seochogu, gangnamgu,songpagu, gangdonggu], axis = 0)
country_es19 = country_es.groupby(['지역'], as_index=False).mean()

#서북권 은평 서대문 마포
country_wn = pd.concat([enpyeonggu, seodeamungu,mapogu], axis = 0)
country_wn19 = country_wn.groupby(['지역'], as_index=False).mean()

#서남권 강서 양천 구로 영등포 금천 동작 관악
country_ws = pd.concat([gangseogu,yangchengu,gurogu, yeongdungpogu, guomcheonggu,dongjackgu,gwanakgu], axis = 0)
country_ws19 = country_ws.groupby(['지역'], as_index=False).mean()

#도심권 종로 중구 용산
country_ce = pd.concat([jongrogu,junggu,yongsangu], axis = 0)
country_ce19 = country_ce.groupby(['지역'], as_index=False).mean()


#지역 권역 별 그래프 그리기
#동북권
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('동북권 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_en19,ax=axes[0])
axes[0].set_xticklabels(country_en19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_en19,ax=axes[1])
axes[1].set_xticklabels(country_en19.지역.unique(),rotation=45, ha='right')

#동남권
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('동남권 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_es19,ax=axes[0])
axes[0].set_xticklabels(country_es19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_es19,ax=axes[1])
axes[1].set_xticklabels(country_es19.지역.unique(),rotation=45, ha='right')

#서북권
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('서북권 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_wn19,ax=axes[0])
axes[0].set_xticklabels(country_wn19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_wn19,ax=axes[1])
axes[1].set_xticklabels(country_wn19.지역.unique(),rotation=45, ha='right')

#서남권
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('서남권 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_ws19,ax=axes[0])
axes[0].set_xticklabels(country_ws19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_ws19,ax=axes[1])
axes[1].set_xticklabels(country_ws19.지역.unique(),rotation=45, ha='right')

#도심권
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('도심권 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=country_ce19,ax=axes[0])
axes[0].set_xticklabels(country_ce19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=country_ce19,ax=axes[1])
axes[1].set_xticklabels(country_ce19.지역.unique(),rotation=45, ha='right')

---------------------------------------

#5주차 - 망 분리

country_net = Seoul_2019['망'] == '도로변대기'
net = Seoul_2019[country_net]

net_19 = net.groupby(['지역'],as_index=False).mean()
net_adress = net.groupby(['주소'],as_index=False).mean()

#도로변대기 그래프 (지역)
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('도로변대기 미세먼지, 초미세먼지')

sns.barplot(x='지역', y='PM10', data=net_19,ax=axes[0])
axes[0].set_xticklabels(net_19.지역.unique(),rotation=45, ha='right')

sns.barplot(x='지역', y='PM25', data=net_19,ax=axes[1])
axes[1].set_xticklabels(net_19.지역.unique(),rotation=45, ha='right')

#max min 지역을 주소으로 분리(주소로 분리시 주소가 2개 뜨는 곳이 도로변대기를 측정하는 지역)


#동북권 도봉 노원 강북 성북 동대문 중랑 성동 광진
country_en = pd.concat([dobonggu,noonegu,gangbukgu,sengbukgu,dongdeamungu,jungranggu,sengdonggu,gwangjingu], axis = 0)
country_en19 = country_en.groupby(['지역'], as_index=False).mean()
country_ennet = country_en.groupby(['주소'], as_index = False).mean()


#동남권 서초 강남 송파 강동
country_es = pd.concat([seochogu, gangnamgu,songpagu, gangdonggu], axis = 0)
country_es19 = country_es.groupby(['지역'], as_index=False).mean()
country_esnet = country_es.groupby(['주소'], as_index = False).mean()

#서북권 은평 서대문 마포
country_wn = pd.concat([enpyeonggu, seodeamungu,mapogu], axis = 0)
country_wn19 = country_wn.groupby(['지역'], as_index=False).mean()
country_wnnet = country_wn.groupby(['주소'], as_index = False).mean()

#서남권 강서 양천 구로 영등포 금천 동작 관악
country_ws = pd.concat([gangseogu,yangchengu,gurogu, yeongdungpogu, guomcheonggu,dongjackgu,gwanakgu], axis = 0)
country_ws19 = country_ws.groupby(['지역'], as_index=False).mean()
country_wsnet = country_ws.groupby(['주소'], as_index = False).mean()

#도심권 종로 중구 용산
country_ce = pd.concat([jongrogu,junggu,yongsangu], axis = 0)
country_ce19 = country_ce.groupby(['지역'], as_index=False).mean()
country_cenet = country_ce.groupby(['주소'], as_index = False).mean()

fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('도심권 미세먼지, 초미세먼지(도로변대기, 도시대기)')

sns.barplot(x='주소', y='PM10', data= country_cenet,ax=axes[0])
axes[0].set_xticklabels(country_cenet.주소.unique(),rotation=45, ha='right')

sns.barplot(x='주소', y='PM25', data=country_cenet,ax=axes[1])
axes[1].set_xticklabels(country_cenet.주소.unique(),rotation=45, ha='right')



#강남구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('강남구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= gangnamgu,ax=axes[0])
axes[0].set_xticklabels(gangnamgu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=gangnamgu,ax=axes[1])
axes[1].set_xticklabels(gangnamgu.망.unique(),rotation=45, ha='right')

#강동구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('강동구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= gangdonggu,ax=axes[0])
axes[0].set_xticklabels(gangdonggu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=gangdonggu,ax=axes[1])
axes[1].set_xticklabels(gangdonggu.망.unique(),rotation=45, ha='right')

#강서구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('강서구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= gangseogu,ax=axes[0])
axes[0].set_xticklabels(gangseogu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=gangseogu,ax=axes[1])
axes[1].set_xticklabels(gangseogu.망.unique(),rotation=45, ha='right')

#금천구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('금천구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= guomcheonggu,ax=axes[0])
axes[0].set_xticklabels(guomcheonggu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=guomcheonggu,ax=axes[1])
axes[1].set_xticklabels(guomcheonggu.망.unique(),rotation=45, ha='right')

#노원구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('노원구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= noonegu,ax=axes[0])
axes[0].set_xticklabels(noonegu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=noonegu,ax=axes[1])
axes[1].set_xticklabels(noonegu.망.unique(),rotation=45, ha='right')

#동대문구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('동대문구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= dongdeamungu,ax=axes[0])
axes[0].set_xticklabels(dongdeamungu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=dongdeamungu,ax=axes[1])
axes[1].set_xticklabels(dongdeamungu.망.unique(),rotation=45, ha='right')


#동작구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('동작구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= dongjackgu,ax=axes[0])
axes[0].set_xticklabels(dongjackgu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=dongjackgu,ax=axes[1])
axes[1].set_xticklabels(dongjackgu.망.unique(),rotation=45, ha='right')


#마포구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('마포구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= mapogu,ax=axes[0])
axes[0].set_xticklabels(mapogu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=mapogu,ax=axes[1])
axes[1].set_xticklabels(mapogu.망.unique(),rotation=45, ha='right')

#서초구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('서초구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= seochogu,ax=axes[0])
axes[0].set_xticklabels(seochogu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=seochogu,ax=axes[1])
axes[1].set_xticklabels(seochogu.망.unique(),rotation=45, ha='right')


#성동구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('성동구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= sengdonggu,ax=axes[0])
axes[0].set_xticklabels(sengdonggu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=sengdonggu,ax=axes[1])
axes[1].set_xticklabels(sengdonggu.망.unique(),rotation=45, ha='right')


#성북구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('성북구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= sengbukgu,ax=axes[0])
axes[0].set_xticklabels(sengbukgu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=sengbukgu,ax=axes[1])
axes[1].set_xticklabels(sengbukgu.망.unique(),rotation=45, ha='right')


#영등포구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('영등포구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= yeongdungpogu,ax=axes[0])
axes[0].set_xticklabels(yeongdungpogu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=yeongdungpogu,ax=axes[1])
axes[1].set_xticklabels(yeongdungpogu.망.unique(),rotation=45, ha='right')


#용산구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('용산구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= yongsangu,ax=axes[0])
axes[0].set_xticklabels(yongsangu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=yongsangu,ax=axes[1])
axes[1].set_xticklabels(yongsangu.망.unique(),rotation=45, ha='right')

#종로구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('종로구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= jongrogu,ax=axes[0])
axes[0].set_xticklabels(jongrogu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=jongrogu,ax=axes[1])
axes[1].set_xticklabels(jongrogu.망.unique(),rotation=45, ha='right')

#중구
fig,axes = plt.subplots(ncols = 2,sharey = True, figsize = (10,5))
fig.suptitle('중구 미세먼지, 초미세먼지')

sns.barplot(x='망', y='PM10', data= junggu,ax=axes[0])
axes[0].set_xticklabels(junggu.망.unique(),rotation=45, ha='right')

sns.barplot(x='망', y='PM25', data=junggu,ax=axes[1])
axes[1].set_xticklabels(junggu.망.unique(),rotation=45, ha='right')









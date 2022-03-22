# -*- coding: utf-8 -*-
"""
02.미세먼지 3주차
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

"""데이터 불러오기"""

train_1 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_1.xlsx')
train_2 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_2.xlsx')
train_3 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_3.xlsx')
train_4 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_4.xlsx')
train_5 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_5.xlsx')
train_6 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_6.xlsx')
train_7 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_7.xlsx')
train_8 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_8.xlsx')
train_9 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_9.xlsx')
train_10 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_10.xlsx')
train_11 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_11.xlsx')
train_12 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019_12.xlsx')

train_1_1 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_1.xlsx')
train_2_2 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_2.xlsx')
train_3_3 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_3.xlsx')
train_4_4 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_4.xlsx')
train_5_5 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_5.xlsx')
train_6_6 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020_6.xlsx')


-----------------------------------2019 2020 월 평균 데이터 한번에 보기


df_2019_aver = pd.concat([np.mean(train_1),np.mean(train_2),np.mean(train_3),np.mean(train_4)
,np.mean(train_5),np.mean(train_6),np.mean(train_7),np.mean(train_8)
,np.mean(train_9),np.mean(train_10),np.mean(train_11),np.mean(train_12)] , axis = 1).transpose()

df_2019_aver.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)

df_2020_aver = pd.concat([np.mean(train_1_1),np.mean(train_2_2),np.mean(train_3_3)
,np.mean(train_4_4),np.mean(train_5_5),np.mean(train_6_6)], axis = 1).transpose()

df_2020_aver.insert(0,"월",[1,2,3,4,5,6],True)


df_2020_aver.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 2020")
plt.xlabel("Month")
plt.ylabel("SO2")

df_2020_aver.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 2020")
plt.xlabel("Month")
plt.ylabel("CO")

df_2020_aver.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 2020")
plt.xlabel("Month")
plt.ylabel("O3")

df_2020_aver.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 2020")
plt.xlabel("Month")
plt.ylabel("NO2")

df_2020_aver.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 2020")
plt.xlabel("Month")
plt.ylabel("PM10")

df_2020_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM2.5 in 2020")
plt.xlabel("Month")
plt.ylabel("PM25")

df_2020_aver.groupby('월')['PM10'].mean().plot()
df_2020_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 , PM10 in 2020")
plt.xlabel("Month")
plt.ylabel("PM25, PM10")

df_2020_aver.groupby('PM10')['PM2.5'].mean().plot()
plt.title("Average PM2.5 based on PM10 in 2020")
plt.xlabel("PM10")
plt.ylabel("PM25")


------------------------------------------------2019, 2020 비교

df_2019_aver.groupby('월')['아황산가스'].mean().plot()
df_2020_aver.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("SO2")

df_2019_aver.groupby('월')['일산화탄소'].mean().plot()
df_2020_aver.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("CO")

df_2019_aver.groupby('월')['오존'].mean().plot()
df_2020_aver.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("O3")

df_2019_aver.groupby('월')['이산화질소'].mean().plot()
df_2020_aver.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("NO2")

df_2019_aver.groupby('월')['PM10'].mean().plot()
df_2020_aver.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("PM10")

df_2019_aver.groupby('월')['PM2.5'].mean().plot()
df_2020_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("PM25")



---------------------------------------지역구대로 나누기

a = train_1['시도'] == '부산 중구'
b = train_2['시도'] == '부산 중구'
c = train_3['시도'] == '부산 중구'
d = train_4['시도'] == '부산 중구'
e = train_5['시도'] == '부산 중구'
f = train_6['시도'] == '부산 중구'
g = train_7['시도'] == '부산 중구'
h = train_8['시도'] == '부산 중구'
i = train_9['시도'] == '부산 중구'
j = train_10['시도'] == '부산 중구'
k = train_11['시도'] == '부산 중구'
l = train_12['시도'] == '부산 중구'

부산_중구_1 = train_1[a]
부산_중구_2 = train_2[b]
부산_중구_3 = train_3[c]
부산_중구_4 = train_4[d]
부산_중구_5 = train_5[e]
부산_중구_6 = train_6[f]
부산_중구_7 = train_7[g]
부산_중구_8 = train_8[h]
부산_중구_9 = train_9[i]
부산_중구_10 = train_10[j]
부산_중구_11 = train_11[k]
부산_중구_12 = train_12[l]

부산_중구 = pd.concat([np.mean(부산_중구_1),np.mean(부산_중구_2),np.mean(부산_중구_3),np.mean(부산_중구_4)
,np.mean(부산_중구_5),np.mean(부산_중구_6),np.mean(부산_중구_7),np.mean(부산_중구_8)
,np.mean(부산_중구_9),np.mean(부산_중구_10),np.mean(부산_중구_11),np.mean(부산_중구_12)] , axis = 1).transpose()

부산_중구.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)


부산_중구.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("SO2")

부산_중구.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 부산 중구")
plt.xlabel("Month")
plt.ylabel("CO")

부산_중구.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("O3")

부산_중구.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("NO2")

부산_중구.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("PM10")

부산_중구.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("PM25")

부산_중구.groupby('월')['PM10'].mean().plot()
부산_중구.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 부산 중구")
plt.xlabel("Month")
plt.ylabel("PM25")



a = train_1['시도'] == '부산 영도구'
b = train_2['시도'] == '부산 영도구'
c = train_3['시도'] == '부산 영도구'
d = train_4['시도'] == '부산 영도구'
e = train_5['시도'] == '부산 영도구'
f = train_6['시도'] == '부산 영도구'
g = train_7['시도'] == '부산 영도구'
h = train_8['시도'] == '부산 영도구'
i = train_9['시도'] == '부산 영도구'
j = train_10['시도'] == '부산 영도구'
k = train_11['시도'] == '부산 영도구'
l = train_12['시도'] == '부산 영도구'

부산_영도구_1 = train_1[a]
부산_영도구_2 = train_2[b]
부산_영도구_3 = train_3[c]
부산_영도구_4 = train_4[d]
부산_영도구_5 = train_5[e]
부산_영도구_6 = train_6[f]
부산_영도구_7 = train_7[g]
부산_영도구_8 = train_8[h]
부산_영도구_9 = train_9[i]
부산_영도구_10 = train_10[j]
부산_영도구_11 = train_11[k]
부산_영도구_12 = train_12[l]

부산_영도구 = pd.concat([np.mean(부산_영도구_1),np.mean(부산_영도구_2),np.mean(부산_영도구_3),np.mean(부산_영도구_4)
,np.mean(부산_영도구_5),np.mean(부산_영도구_6),np.mean(부산_영도구_7),np.mean(부산_영도구_8)
,np.mean(부산_영도구_9),np.mean(부산_영도구_10),np.mean(부산_영도구_11),np.mean(부산_영도구_12)] , axis = 1).transpose()

부산_영도구.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)



부산_영도구.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("SO2")

부산_영도구.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("CO")

부산_영도구.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("O3")

부산_영도구.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("NO2")

부산_영도구.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("PM10")

부산_영도구.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("PM25")

부산_영도구.groupby('월')['PM10'].mean().plot()
부산_영도구.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 부산 영도구")
plt.xlabel("Month")
plt.ylabel("PM25")

----------------------------------------- 종강 후
#2018 데이터 취합
train_111 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_1.xlsx')
train_222 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_2.xlsx')
train_333 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_3.xlsx')
train_444 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_4.xlsx')
train_555 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_5.xlsx')
train_666 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_6.xlsx')
train_777 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_7.xlsx')
train_888 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_8.xlsx')
train_999 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_9.xlsx')
train_1000 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_10.xlsx')
train_1111 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_11.xlsx')
train_1212 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018_12.xlsx')

train_2018 = pd.concat([train_111,train_222,train_333,train_444,train_555
,train_666,train_777,train_888,train_999,train_1000,train_1111,train_1212], axis = 0)

train_2018.to_excel(excel_writer='C:/Users/juyeo/Desktop/microdust/2018_12.xlsx')

#2019 데이터 취합
train_2019 = pd.concat([train_1,train_2,train_3,train_4,train_5
,train_6,train_7,train_8,train_9,train_10,train_11,train_12], axis = 0)

train_2019.to_excel(excel_writer='2019.xlsx')

#2020 데이터 취합
train_2020 = pd.concat([train_1_1,train_2_2,train_3_3,train_4_4,train_5_5
,train_6_6], axis = 0)

train_2020.to_excel(excel_writer='2020.xlsx')

#분산 그래프 그리기
df_2019_var = pd.concat([np.var(train_1),np.var(train_2),np.var(train_3),np.var(train_4)
,np.var(train_5),np.var(train_6),np.var(train_7),np.var(train_8)
,np.var(train_9),np.var(train_10),np.var(train_11),np.var(train_12)] , axis = 1).transpose()

df_2019_var.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)

df_2020_var = pd.concat([np.var(train_1_1),np.var(train_2_2),np.var(train_3_3)
,np.var(train_4_4),np.var(train_5_5),np.var(train_6_6)], axis = 1).transpose()

df_2020_var.insert(0,"월",[1,2,3,4,5,6],True)



df_2019_var.groupby('월')['PM10'].var().plot()
df_2020_var.groupby('월')['PM10'].var().plot()
plt.title("Monthly var of PM10 in 2019, 2020")
plt.xlabel("Month")
plt.ylabel("PM10")

#2019년 미세먼지, 초미세먼지 분산
df_2019_var.groupby('월')['PM10'].mean().plot()
df_2019_var.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly var of PM10, PM25 in 2019")
plt.xlabel("Month")
plt.ylabel("PM10, PM25")

#2019년 3월 미세먼지, 초미세먼지 분산
#날짜에서 시간 없애기
train_3['PM10'].isnull().sum()
아황산가스    2350
일산화탄소    2366
오존        137
이산화질소     145
PM10      126
PM2.5      74
dtype: int64

train_3 = train_3.interpolate()



train_3['날짜'] = train_3['날짜'] +['']
train_3.drop(['날짜'], axis=1)


train_3.groupby('날짜')['PM10'].plot()
#2019년 9월 미세먼지, 초미세먼지 분산

#2019년 3월 미세먼지, 초미세먼지 평균
train_3.groupby('날짜')['PM10'].plot()


#2019년 9월 미세먼지, 초미세먼지 평균

-------------------------------2018

df_2018_aver = pd.concat([np.mean(train_111),np.mean(train_222),np.mean(train_333),np.mean(train_444)
,np.mean(train_555),np.mean(train_666),np.mean(train_777),np.mean(train_888)
,np.mean(train_999),np.mean(train_1000),np.mean(train_1111),np.mean(train_1212)] , axis = 1).transpose()

df_2018_aver.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)


df_2018_var = pd.concat([np.var(train_111),np.var(train_222),np.var(train_333),np.var(train_444)
,np.var(train_555),np.var(train_666),np.var(train_777),np.var(train_888)
,np.var(train_999),np.var(train_1000),np.var(train_1111),np.var(train_1212)] , axis = 1).transpose()

df_2018_var.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)

#평균

df_2018_aver.groupby('월')['아황산가스'].mean().plot()
df_2019_aver.groupby('월')['아황산가스'].mean().plot()
df_2020_aver.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("SO2")
plt.legend(loc='upper right')

df_2018_aver.groupby('월')['일산화탄소'].mean().plot()
df_2019_aver.groupby('월')['일산화탄소'].mean().plot()
df_2020_aver.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("CO")
plt.legend(loc='upper right')

df_2018_aver.groupby('월')['오존'].mean().plot()
df_2019_aver.groupby('월')['오존'].mean().plot()
df_2020_aver.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("O3")
plt.legend(loc='upper right')

df_2018_aver.groupby('월')['이산화질소'].mean().plot()
df_2019_aver.groupby('월')['이산화질소'].mean().plot()
df_2020_aver.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("NO2")
plt.legend(loc='upper right')

df_2018_aver.groupby('월')['PM10'].mean().plot()
df_2019_aver.groupby('월')['PM10'].mean().plot()
df_2020_aver.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("PM10")
plt.legend(loc='upper right')

df_2018_aver.groupby('월')['PM2.5'].mean().plot()
df_2019_aver.groupby('월')['PM2.5'].mean().plot()
df_2020_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("PM25")
plt.legend(loc='upper right')

------------------------------
#분산 

df_2018_var.groupby('월')['아황산가스'].mean().plot()
df_2019_var.groupby('월')['아황산가스'].mean().plot()
df_2020_var.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly var of SO2 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("SO2")
plt.legend(loc='upper right')

df_2018_var.groupby('월')['일산화탄소'].mean().plot()
df_2019_var.groupby('월')['일산화탄소'].mean().plot()
df_2020_var.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly var of CO in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("CO")
plt.legend(loc='upper right')

df_2018_var.groupby('월')['오존'].mean().plot()
df_2019_var.groupby('월')['오존'].mean().plot()
df_2020_var.groupby('월')['오존'].mean().plot()
plt.title("Monthly var of O3 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("O3")
plt.legend(loc='upper right')

df_2018_var.groupby('월')['이산화질소'].mean().plot()
df_2019_var.groupby('월')['이산화질소'].mean().plot()
df_2020_var.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly var of NO2 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("NO2")
plt.legend(loc='upper right')

df_2018_var.groupby('월')['PM10'].mean().plot()
df_2019_var.groupby('월')['PM10'].mean().plot()
df_2020_var.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("PM10")
plt.legend(loc='upper right')

df_2018_var.groupby('월')['PM2.5'].mean().plot()
df_2019_var.groupby('월')['PM2.5'].mean().plot()
df_2020_var.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 2018,2019,2020")
plt.xlabel("Month")
plt.ylabel("PM25")
plt.legend(loc='upper right')


# -*- coding: utf-8 -*-
"""
02.미세먼지 2주차

2019년 전체 평균 2020 전체 평균 비교
2019년 월별 평균 그래프

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

df = pd.DataFrame()

train_1.index
train_1.columns

#2019년 평균
#year_mean= np.mean(train_1)+np.mean(train_2)+np.mean(train_3)+np.mean(train_4)
+np.mean(train_5)+np.mean(train_6)+np.mean(train_7)+np.mean(train_8)
+np.mean(train_9)+np.mean(train_10)+np.mean(train_11)+np.mean(train_12)


a = np.mean(train_1+train_2+train_3+train_4+train_5+train_6+train_7+train_8+train_9+train_10+train_11+train_12)
a = a/12

측정소코드    221213.136364
아황산가스         0.004050
일산화탄소         0.465353
오존            0.018000
이산화질소         0.026471
PM10         35.016127
PM2.5        22.871476
dtype: float64

b= np.mean(train_1_1+train_2_2+train_3_3+train_4_4+train_5_5+train_6_6)
b = b/12

측정소코드    110599.751959
아황산가스         0.001815
일산화탄소         0.184495
오존            0.017196
이산화질소         0.008210
PM10         16.144424
PM2.5         8.989106
dtype: float64



#2019 월 평균 데이터 한번에 보기
df_2019_aver = pd.concat([np.mean(train_1),np.mean(train_2),np.mean(train_3),np.mean(train_4)
,np.mean(train_5),np.mean(train_6),np.mean(train_7),np.mean(train_8)
,np.mean(train_9),np.mean(train_10),np.mean(train_11),np.mean(train_12)] , axis = 1).transpose()

df_2019_aver.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)

df_2019_aver.groupby('월')['아황산가스'].mean().plot()
plt.title("Monthly average of SO2 in 2019")
plt.xlabel("Month")
plt.ylabel("SO2")

df_2019_aver.groupby('월')['일산화탄소'].mean().plot()
plt.title("Monthly average of CO in 2019")
plt.xlabel("Month")
plt.ylabel("CO")

df_2019_aver.groupby('월')['오존'].mean().plot()
plt.title("Monthly average of O3 in 2019")
plt.xlabel("Month")
plt.ylabel("O3")

df_2019_aver.groupby('월')['이산화질소'].mean().plot()
plt.title("Monthly average of NO2 in 2019")
plt.xlabel("Month")
plt.ylabel("NO2")

df_2019_aver.groupby('월')['PM10'].mean().plot()
plt.title("Monthly average of PM10 in 2019")
plt.xlabel("Month")
plt.ylabel("PM10")

df_2019_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 in 2019")
plt.xlabel("Month")
plt.ylabel("PM25")


df_2019_aver.groupby('월')['PM10'].mean().plot()
df_2019_aver.groupby('월')['PM2.5'].mean().plot()
plt.title("Monthly average of PM25 , PM10 in 2019")
plt.xlabel("Month")
plt.ylabel("PM25, PM10")

df_2019_aver.groupby('PM10')['PM2.5'].mean().plot()
plt.title("Average PM25 based on PM10 in 2019")
plt.xlabel("PM10")
plt.ylabel("PM25")




"""
plt.plot(df_2019_aver['PM10'],lable = 'PM10')
plt.plot(df_2019_aver['PM2.5'], label = 'PM2.5')
plt.legend('upper right')

plt.figure()

"""
------------------------------------------------- 미완성
#2019 분산


df_2019_var = pd.concat([np.var(train_1),np.var(train_2),np.var(train_3),np.var(train_4)
,np.var(train_5),np.var(train_6),np.var(train_7),np.var(train_8)
,np.var(train_9),np.var(train_10),np.var(train_11),np.var(train_12)], axis = 1).transpose()

df_2019_var.insert(0,"월",[1,2,3,4,5,6,7,8,9,10,11,12],True)

#2020 월 데이터 평균 한번에 보기

df_2019_var.groupby('월')['아황산가스'].var().plot()


df_2020_aver = pd.concat([np.mean(train_1_1),np.mean(train_2_2),np.mean(train_3_3)
,np.mean(train_4_4),np.mean(train_5_5),np.mean(train_6_6)], axis = 1).transpose()

df_2020_aver.insert(0,"월",[1,2,3,4,5,6],True)










"""
02.미세먼지 3주차 개강 이후 코딩
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#데이터 불러오기

train_2018 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2018.xlsx')
train_2019 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2019.xlsx')
train_2020 = pd.read_excel('C:/Users/juyeo/Desktop/microdust/2020.xlsx')

#결측값 확인
train_2018.isnull().sum()

아황산가스         31127
일산화탄소         30895
오존             5110
이산화질소          5485
PM10           4952
PM2.5          4567
dtype: int64

train_2019.isnull().sum()

아황산가스         30796
일산화탄소         30535
오존             4803
이산화질소          4666
PM10           4196
PM2.5          3574
dtype: int64

train_2020.isnull().sum()

시도             8784
측정소명              0
측정소코드             0
아황산가스         17261
일산화탄소         17224
오존             1710
이산화질소          1423
PM10           1443
PM2.5          1154
dtype: int64

#결측값 채우기 (선형)
train_2018 = train_2018.interpolate()
train_2018.isnull().sum()

train_2019 = train_2019.interpolate()
train_2019.isnull().sum()

train_2020 = train_2020.interpolate()
train_2020.isnull().sum()

#
train_2018.mean()
Unnamed: 0      7115.736486
측정소코드         221204.005912
아황산가스              0.004874
일산화탄소              0.360134
오존                 0.029012
이산화질소              0.018985
PM10              41.339838
PM2.5             22.875601
dtype: float64

train_18_1 = train_2018.to_














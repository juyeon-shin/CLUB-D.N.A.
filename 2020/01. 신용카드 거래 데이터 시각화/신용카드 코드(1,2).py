import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime

'''
date : 거래일자
time : 거래시간
card_id : 카드 번호의 hash 값
amount : 매출액, 0보다 작은 음수는 거래 취소(환불)
istallments : 할부개월수. 일시불은 빈 문자열
days_of_week : 요일, 월요일이 0, 일요일은 6
holyday : 1이면 공휴일, 0이면 공휴일 아님
'''

#1.데이터 불러오기

train = pd.read_csv('train_juyeon.csv')
train.installments.unique()
train.head()

#2. 결측치 확인, 결측치 보간
train.isna().sum()
train.installments.fillna(0, inplace = True)
train.installments.isna().sum()

df = pd.DataFrame()

df['date'] = train['date']
df['time'] = train['time']
df['amount'] = train['amount']
df['days_of_week'] = train['days_of_week']
df['holyday'] = train['holyday']
#df['hour'] = df['time'].hour 
# (시리즈를 데이트타임으로 만들 수 없다?)

#시간대별 매출액 평균 
df.groupby('time')['amount'].mean().plot()
plt.title("amount by time (mean)")
plt.xlabel("time")
plt.ylabel("amount")

#시간대별 매출액 분산
df.groupby('time')['amount'].var().plot()
plt.title("amount by time (var)")
plt.xlabel("time")
plt.ylabel("amount")

#시간대별 판매량
df.groupby('time')['amount'].count().plot.kde()
plt.title("amount by time (count)")
plt.xlabel("time")
plt.ylabel("amount")

df_1 = pd.DataFrame()
df_1['store_id'] = train['store_id']
df_1['amount'] = train['amount']
df_1['installments'] = train['installments']

#상점별 매출액 평균
df_1.groupby('store_id')['amount'].mean().plot()
plt.title("amount by store_id (mean)")
plt.xlabel("store_id")
plt.ylabel("amount")

#상점별 매출액 분산
df_1.groupby('store_id')['amount'].var().plot()
plt.title("amount by store_id (var)")
plt.xlabel("store_id")
plt.ylabel("amount")

#상점별 판매량
df_1.groupby('store_id')['amount'].count().plot.kde()
plt.title("amount by store_id (count)")
plt.xlabel("store_id")
plt.ylabel("amount")

#휴일별 매출액 평균
df.groupby('holyday')['amount'].mean().plot(kind = 'bar')
plt.title("amount by holyday (mean)")
plt.xlabel("holyday")
plt.ylabel("amount")

#휴일별 판매량
df.groupby('holyday')['amount'].count().plot(kind = 'bar')
plt.title("amount by holyday (count)")
plt.xlabel("holyday")
plt.ylabel("amount")

#요일별 매출액 평균
df.groupby('days_of_week')['amount'].mean().plot(kind = 'bar')
plt.title("amount by week (mean)")
plt.xlabel("week")
plt.ylabel("amount")

#요일별 판매량
df.groupby('days_of_week')['amount'].count().plot(kind = 'bar')
plt.title("amount by week (count)")
plt.xlabel("store_id")
plt.ylabel("amount")
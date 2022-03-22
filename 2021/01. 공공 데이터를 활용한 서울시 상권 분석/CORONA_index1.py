# -*- coding: utf-8 -*-
"""

CORONA : index1

"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

index1 =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/index.csv')

'''
품목 별 소비지수 데이터

period = 기준월
catl = 대분류
catm = 중분류
age = 나이대
gender = 성별
sido = 지역
sigungu = 세부지역
cgi = 카테고리성장지수 (2018년 월평균 대비 매출 성장 비율, 100을 기준으로 이상이면 매출 상승, 이하면 하락)
'''

'''--------------------1 week-------------------'''

index1.isnull().sum() #결측값 없음

period_cnt = index1.groupby(['period']).count()            #period : 201901 ~ 202005, 약 7400~7600개의 데이터
catl_cnt = index1.groupby(['catl']).count()                #catl : 식품이 가장 많음
age_cnt = index1.groupby(['age']).count()                  # 비슷, all 이 무슨 의미?
sido_cnt = index1.groupby(['sido']).count()                # 서울 데이터만 있음 
sigungu_cnt = index1.groupby(['sigungu']).count()          # 26개의 시군구
gender_cnt = index1.groupby(['gender']).count() 

index1_corr = index1.corr()
sns.heatmap(index1_corr,annot = True, annot_kws={'size' : 20}, square = True, cmap = 'Blues')







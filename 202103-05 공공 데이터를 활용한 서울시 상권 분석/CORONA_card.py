# -*- coding: utf-8 -*-
"""

CORONA : card

"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

card =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/card_20200717.csv')

'''
업종 별 결재금액 데이터

receipt_dttm = 카드회사가 카드사용내역을 접수한일자
adstrd_code = 가맹점 위치 기준 행정동 코드
adstrd_nm = 가맹점 위치 기준 행정동명
mrhst_induty_cl_code = 가맹점 업종코드
mrhst_induty_cl_nm = 가맹점 업종명
selng_cascnt = 매출발생건수
salamt = 매출발생금액
'''

'''--------------------1 week-------------------'''

card.isnull().sum() #결측값 없음

card_dis = card.groupby(['adstrd_nm']).mean()

업종별 기초통계

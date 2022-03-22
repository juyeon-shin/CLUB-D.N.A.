# -*- coding: utf-8 -*-
"""
CORONA 
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


fpopl =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/fpopl.csv',)

'''
행정동별 유동인구 데이터

base_ymd = 기준년월일
tmzon_se_code = 24시간대 구분코드
sexdstn_se_code = 성별 구분코드 (M: 남성, F: 여성)
agrde_se_code = 5세단위 연령대구분코드 (단, age_00: 0세 ~ 9세, age_70: 70세 이상)
adstrd_code = 행정동코드
popltn_cascnt = 인구수
'''

a = fpopl.describe()



adstrd_master =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/adstrd_master.csv')

'''
8자리 행정동 코드 데이터

adstrd_code = 행정동 코드
adstrd_nm = 행정동명
brtc_nm = 시도명
signgu_nm = 시군구명
'''

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
card.isnull().sum() #결측값 없음

card_dis = card.groupby(['adstrd_nm']).mean()

업종별 기초통계




delivery =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/delivery.csv')

'''
배달 호출 정보 데이터

SERIAL_NUMBER = 순번
PROCESS_DT = 처리일시
DLVR_RQESTER_ID = 배달요청업체 ID
DLVR_REQUST_STTUS_VALUE = 배달요청상태값 (1:완료, 2:취소, 3:사고, 4:문의)
DLVR_RCEPT_CMPNY_ID = 배달접수회사 ID
DLVR_STORE_ID = 배달상점ID
DLVR_STORE_INDUTY_NM = 배달상점 업종이름
DLVR_STORE_LEGALDONG_CODE = 배달상점 주소 법정동코드
DLVR_STORE_SIDO = 배달상점 주소 법정동 시도명
DLVR_STORE_SIGUNGU = 배달상점 주소 법정동 시군구명
DLVR_STORE_DONG = 배달상점 주소 법정동 읍면동명
DLVR_STORE_RI = 배달상점 주소 법정동 리명
DLVR_STORE_ADSTRD_CODE = 배달상점 주소 행정동 코드
DLVR_STORE_RDNMADR_CODE = 배달상점주소 도로명주소 코드
DLVR_DSTN_LEGALDONG_CODE = 배달목적지 주소 법정동코드
DLVR_DSTN_SIDO = 배달목적지 주소 법정동 시도명
DLVR_DSTN_SIGUNGU = 배달목적지 주소 법정동 시군구명
DLVR_DSTN_DONG = 배달목적지 주소 법정동 읍면동명
DLVR_DSTN_RI = 배달목적지 주소 법정동 리명
DLVR_DSTN_ADSTRD_CODE = 배달목적지 주소 행정동 코드
DLVR_DSTN_RDNMADR_CODE = 배달목적지주소 도로명주소 코드
DLVR_MAN_ID = 배달기사 ID
DLVR_AMOUNT = 배달비용
CALL_RLAY_FEE_AMOUNT = 호출중계수수료금액
GOODS_AMOUNT = 배달상품금액
SETLE_KND_VALUE = 결제종류번호 (1:카드, 2:선불, 3:현금)
SETLE_CARD_CN = 결제카드종류
DLVR_RCEPT_TIME = 배달접수시간
DLVR_CARALC_TIME = 배달배차시간
DLVR_COMPT_TIME = 배달완료시간
DLVR_CANCL_TIME = 배달취소시간
'''


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

index1.isnull().sum() #결측값 없음
index_dis=index1.describe()
index_cnt = index1.groupby(['age']).count()
index_mean = index1.groupby(['age']).mean()



index = index1['age']== all
index1.tail()

index1_corr = index1.corr()

about_age = index1['age']==20
index_age = about_age[20]

나이대별 기초통계
성별, 지역


CO_time = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/time.csv')

CO_timeage = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/timeage.csv')

CO_timegender= pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/timegender.csv')

CO_timeprovince = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/timeprovince.csv')

CO_region =pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/region.csv')

CO_policy = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/policy.csv')

CO_case = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/case.csv')

CO_patientinfo = pd.read_csv('C:/Users/juyeo/Desktop/CORONA/KT_data_20200717/COVID_19/patientinfo_20200717.csv')


'''---------------------------------------------'''






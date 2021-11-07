# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:35:08 2021

@author: qkrfo
"""

#인덱스 활용

import pandas as pd

exam_data = {'이름' : ['서준', '우현' , '인아'],
             '수학' : [90,80,70],
             '영어' : [98,89,95],
             '음악' : [85,95,100],
             '체육' : [100,90,90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

ndf = df.set_index(['이름'])
print(ndf)
print('\n')
ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')
ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)
print('\n')

#새로운 배열로 행 인덱스 재지정

dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}

df2 = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df2)
print('\n')

new_index = ['r0','r1','r2','r3','r4']
ndf = df2.reindex(new_index)
print(ndf)
print('\n')

new_index = ['r0','r1','r2','r3','r4']
ndf2 = df2.reindex(new_index, fill_value = 0)
print(ndf2)
print('\n')

#정수형 위치 인덱스 초기화
ndf3 = df2.reset_index()
print(ndf3)
print('\n')

#행 인덱스를 기준으로 데이터프레임 정렬
ndf4 = df2.sort_index(ascending=False)
print(ndf4)
print('\n')

#열 기준 내림차순 정렬
ndf5 = df2.sort_values(by='c1',ascending=False)
print(ndf5)
print('\n') 
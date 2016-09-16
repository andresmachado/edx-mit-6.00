# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:23:59 2016

@author: andre
"""
num = int(input("Choose a number to convert: "))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False   
result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result
print(result)
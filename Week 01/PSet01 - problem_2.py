# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:31:06 2016

@author: andre

Problem 2

(10/10 points)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2

"""

s = 'azcbobobegghakl'

word = 'bob'
num_of_bobs = 0

for char in range(0, len(s)):
    a_word = s[char:char+len(word)]
    
    if a_word == 'bob':
        num_of_bobs += 1

print('Number of times bob occurs is:', num_of_bobs)

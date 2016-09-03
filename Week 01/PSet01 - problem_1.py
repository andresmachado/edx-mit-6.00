# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:14:22 2016

@author: andre

Problem 1

(10/10 points)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

vowels = 'aeiou'
num_of_vowels = 0

for char in s:
    if char in vowels:
        num_of_vowels += 1
print(num_of_vowels)
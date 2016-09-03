# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 19:37:13 2016

@author: andre
----------------------------
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print:

"Longest substring in alphabetical order is: beggh"

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = 'azcbobobegghakl'

bestMatch = s[0]
testString = s[0]

for i in range (1, len(s)):
    
    if s[i] >= s[i-1]:
        testString += s[i]       
    else:
        testString = s[i]
        
    if len(testString) > len(bestMatch):
        bestMatch = testString
               
print("Longest substring in alphabetical order is: " + bestMatch)
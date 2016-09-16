# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:53:07 2016

@author: andre
"""

import math

def polysum(n, s):
    
    area = (0.25 * n) * s**2 / math.tan(math.pi/n)
    perimeter = (n * s)**2
    return round(area + perimeter, 4) # return result rounded to 4 places
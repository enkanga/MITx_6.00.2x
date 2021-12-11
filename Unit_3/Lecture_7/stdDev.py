# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:41:39 2021

@author: ENkanga
"""

def stdDev(L):
    N = len(L)
    mu = sum(L) / N
    
    sum_sq_dev = 0
    for l in L:
        sum_sq_dev += (l - mu) ** 2
    
    return (sum_sq_dev / N) ** .5


        
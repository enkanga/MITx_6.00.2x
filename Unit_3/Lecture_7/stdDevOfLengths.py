# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:25:29 2021

@author: ENkanga
"""

'''
Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
and outputs the standard deviation of the lengths of the strings. 
Return float('NaN') if L is empty.
'''

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    N = len(L)
    if N == 0:
        return float('NaN') 
    
    total_lengths = 0
    for s in L:
        total_lengths += len(s)
    mu = total_lengths / N
    
    sum_dev = 0
    for s in L:
        sum_dev += (len(s) - mu) ** 2
    
    return (sum_dev / N) ** .5


print(f"L = ['a', 'z', 'p']: {stdDevOfLengths(['a', 'z', 'p'])}")
print(f"L = ['apples', 'oranges', 'kiwis', 'pineapples']: {stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])}")


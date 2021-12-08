# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:05:26 2021

@author: ENkanga
"""

'''
Write a deterministic program, deterministicNumber, 
that returns an even number between 9 and 21.
'''

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 18

'''
Write a uniformly distributed stochastic program, stochasticNumber, 
that returns an even number between 9 and 21.
'''

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    return random.randrange(10, 22, 2)
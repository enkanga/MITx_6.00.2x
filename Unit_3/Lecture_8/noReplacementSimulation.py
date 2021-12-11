# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:49:09 2021

@author: ENkanga
"""

'''
You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, 
you don't replace it. What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. 
Feel free to write a helper function if you wish.
'''

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    all_same_color = 0
    
    for t in range(numTrials):
        balls = ['r', 'r', 'r', 'g', 'g', 'g']
        draws = []
        
        for i in range(3):
            draw = random.choice(balls)
            draws.append(draw)
            balls.remove(draw)
        
        if draws[0] == draws[1] and draws[0] == draws[2]:
            all_same_color += 1
    
    return all_same_color / numTrials


for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    print(f'% of times 3 balls of the same color were drawn: {noReplacementSimulation(i)}, Number of trials: {i}')

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:58:20 2021

@author: ENkanga
"""

'''
Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, 
as well as the parameters from Edge. You should additionally include a getWeight method. 
The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".
'''


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.getWeight()) + ')'

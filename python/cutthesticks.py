#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

"""
You are given a number of sticks of varying lengths. You will iteratively cut the sticks 
into smaller sticks, discarding the shortest pieces until there are none left. At each 
iteration you will determine the length of the shortest stick remaining, cut that length 
from each of the longer sticks and then discard all the pieces of that shortest length. 
When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration 
until there are none left.

For example, there are n = 3 sticks of lengths arr = [1, 2, 3]. The shortest stick length 
is 1, so we cut that length from the longer two and discard the pieces of length 1. Now our 
lengths are arr = [1, 2]. Again, the shortest stick is of length 1, so we cut that amount 
from the longer stick and discard those pieces. There is only one stick left, arr = [1], so 
we discard that stick. Our lengths are answer = [ 3, 2, 1].

Link: https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        lengthOfCut = min(arr)

        # cat the sticks
        tmp = list(map(lambda x : x - lengthOfCut, arr))

        # remove the sticks        
        arr = [x for x in tmp if x > 0]

    return result

if __name__ == '__main__':
    # sample case 1
    #n = 6
    #arr = [ 5, 4, 4, 2, 2, 8 ]

    # sample case 2
    n = 8
    arr = [ 1, 2, 3, 4, 3, 3, 2, 1 ]

    result = cutTheSticks(arr)
    print(np.array(result))

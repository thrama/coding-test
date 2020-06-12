#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals. 

Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

def diagonalDifference(arr):
    # Write your code here
    print(np.matrix(arr))
    dim = len(arr[0])

    # first diagonal, from 0,0 to n,n
    d1 = 0
    for i in range(dim):
        d1 += arr[i][i]
    print(d1)

    # opposit diagonal
    d2 = 0 
    for i in range(dim):
        d2 += arr[i][dim - 1 - i]
    print(d2)

    return abs(d1 - d2)




if __name__ == '__main__':

    # sample case
    n = 3
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)
    print(result)
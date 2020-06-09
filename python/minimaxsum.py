#!/bin/python3

import math
import os
import random
import re
import sys

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing 
exactly four of the five integers. Then print the respective minimum and maximum values as a single 
line of two space-separated long integers.
For example, arr=[1,3,5,7,9]. Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9=24. We 
would print: 16 24

Link: https://www.hackerrank.com/challenges/mini-max-sum/problem

"""

def miniMaxSum(arr):

    max_num = max(arr)
    min_num = min(arr)
    max_sum = 0
    min_sum = 0
    
    occurred= False
    for i in range(len(arr)):
        if (arr[i] != max_num):
            min_sum += arr[i]
        else:
            if occurred:
                min_sum += arr[i]
            else:   
                occurred = True
    
    occurred= False
    for i in range(len(arr)):
        if (arr[i] != min_num):
            max_sum += arr[i]
        else:
            if occurred:
                max_sum += arr[i]
            else:
                occurred = True

    print(f"{min_sum} {max_sum}")
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

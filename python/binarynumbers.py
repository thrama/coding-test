#!/bin/python3

import math
import os
import random
import re
import sys

'''
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the 
base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''

if __name__ == '__main__':
    #n = int(input())
    
    # simple case
    n = 439

    # convert decimal to binary
    get_bin = lambda n: format(n, 'b')
    str_bin = str(get_bin(n))
    print(f'bin: {str_bin}')

    temp = 0
    result = 0
    for i in range(len(str_bin)):
        
        if str_bin[i] == '1':
            temp += 1
            if temp > result:
                result = temp
        else:
            temp = 0
    print(result)

        


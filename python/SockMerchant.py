#!/bin/python3

import math
import os
import random
import re
import sys

"""
John works at a clothing store. He has a large pile of socks that he must pair 
by color for sale. Given an array of integers representing the color of each 
sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1,2,1,2,1,2,3]. There is 
one pair of color 1 and one of color 2. There are three odd socks left, one 
of each color. The number of pairs is 2.

Link: https://www.hackerrank.com/challenges/sock-merchant/problem
"""

def sockMerchant(n, ar):

    # find unique values in the array
    unique = []
    for i in range(n):
        if not(ar[i] in unique):
            unique.append(ar[i])

    # count the socks paired
    pair = 0
    for i in range(len(unique)):
        x = ar.count(unique[i])
        pair += (x // 2)
            
    # debug
    #print(ar)
    #print(unique)
    #print(pair)

    return pair



if __name__ == '__main__':

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    print(result)

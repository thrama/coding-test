#!/bin/python3

import math
import os
import random
import re
import sys

"""
Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):

    # count the apples on the house
    applesInRange = 0
    for i in apples:
        if (a + i >= s) and (a + i <= t):
            applesInRange += 1

    print(applesInRange)

    # count the oranges on the house
    orangesInRange = 0
    for i in oranges:
        if (b + i >= s) and (b + i <= t):
            orangesInRange += 1

    print(orangesInRange)



if __name__ == '__main__':

    # simple case 1
    #s = 7
    #t = 11

    #a = 5
    #b = 15

    #m = 3
    #n = 2

    #apples = [-2, 2, 1]
    #oranges = [5, -6]

    # simple case 2
    s = 2
    t = 3

    a = 1
    b = 5

    m = 1
    n = 1

    apples = [2]
    oranges = [-2]

    countApplesAndOranges(s, t, a, b, apples, oranges)


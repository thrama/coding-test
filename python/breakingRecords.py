#!/bin/python3

"""
Maria plays college basketball and wants to go pro. Each season she maintains 
a record of her play. She tabulates the number of times she breaks her season 
record for most points and least points in a game. Points scored in the first 
game establish her record for the season, and she begins counting from there.

Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    x = y = 0
    highScore = lowScore = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > highScore:
            highScore = scores[i]
            print(highScore)
            x+=1

        if scores[i] < lowScore:
            lowScore = scores[i]
            y+=1 
        
    return x, y

if __name__ == '__main__':

    #scores = [ 10, 5, 20, 20, 4, 5, 2, 25, 1 ]
    scores = [ 3, 4, 21, 36, 10, 28, 35, 5, 24, 42, ]

    result = breakingRecords(scores)

    print(result)
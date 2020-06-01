#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    c = 0
    print(q)
    for j in range(len(q)):
        for k in range(len(q) - 1):
            if q[k] > q[k + 1]:
                q[k], q[k + 1] = q[k + 1], q[k]
                c += 1
    print(c)  

# solution find at: https://www.martinkysel.com/hackerrank-new-year-chaos-solution/
def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            return "Too chaotic"
        for j in xrange(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    return moves


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

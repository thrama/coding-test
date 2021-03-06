#!/bin/python3

import math
import os
import random
import re
import sys

"""
A Discrete Mathematics professor has a class of  students. Frustrated with their lack of 
discipline, hedecides to cancel class if fewer than students are present when class starts. 
Given the arrival time of each student, determine if the class is canceled.

Link: https://www.hackerrank.com/challenges/angry-professor/
"""

def angryProfessor(k, a):
    for i in range(len(a)):
        # if student are in time, substratct him from the number of threshold
        if int(a[i]) <= 0:
            k -= 1
    
    #print (k)

    # if the treshol is less than zero, the class is cancelled
    if k <= 0:
        return 'NO'
    else: 
        return 'YES'

### sample input
#k = 20
#a = '97 -55 48 -22 99 -46 40 11 5 -61 78 -20 44 22 -8 82 24 -62 0 52 -79 68 -73 -81 33 60 -99 -99 59 -13 90 -26 84 90 76 36 -45 79 87 48 59 -36 42 -6 -13 21 -19 -21 39 -40'.split(' ')
k = 18
a = '-50 58 24 69 81 84 72 50 -85 99 42 13 90 90 -81 -36 55 4 -69 -76 55 42 -84 -5 -67 13 -54 59 2 6 21 68 89 8 98 8 -48 -33 -48 54 -46 29 46 97 -90 -33 -97 -92 25 96'.split(' ')
#k = 26
#a = '-36 14 -60 28 -50 56 94 -99 -39 28 0 -47 59 -35 39 15 -4 -49 85 -43 -77 38 -49 -67 92 -43 29 82 41 -26 61 60 -23 -81 -90 -96 -77 90 24 -14 5 12 0 26 16 78 -46 47 51 31'.split(' ')
#k = 44
#a = '86 55 90 79 69 -74 -41 33 -88 66 84 17 60 -37 -59 -18 -83 -58 -37 -83 -78 -14 -29 59 38 -88 33 -81 -58 99 -39 -63 94 -47 -62 90 91 -15 -57 91 -51 -21 -40 30 25 -16 2 -39 4 80'.split(' ')
#k = 19
#a = '2 -77 -36 76 -7 -57 99 -27 36 18 -63 -44 -5 91 -55 89 93 5 22 17 93 26 -86 -43 14 -79 -62 -88 -10 94 -46 -37 -53 -73 25 -10 17 63 -90 30 71 -33 -89 -4 -5 68 -85 95 -49 67'.split(' ')
#k = 27
#a = '81 -60 55 18 -42 96 -21 84 27 40 -72 30 -47 30 -14 -22 -24 35 4 43 86 78 -62 83 -48 -24 22 35 -57 -47 -76 -18 -3 -33 -59 6 -20 8 98 -76 15 71 -59 10 24 -39 78 -53 -14 89'.split(' ')
#k = 27
#a = '-87 -32 81 -50 -90 50 -13 -94 -81 -20 -82 -87 -96 -4 92 -97 34 -6 -57 95 -62 -83 54 -9 -32 21 63 82 -85 85 90 -14 16 92 -28 -25 36 18 -37 82 -10 -88 -15 37 -8 83 57 -27 69 -51'.split(' ')
#k = 50
#a = '-98 10 -77 76 -52 -87 -99 -66 17 -35 98 95 5 28 28 93 97 -72 45 25 -83 27 21 -34 -34 -59 -57 61 72 -16 50 82 -17 73 -6 -64 63 -72 -37 -28 -80 -56 41 52 -11 -17 -83 -12 6 67'.split(' ')
#k = 15
#a = '4 -79 -12 69 70 44 49 65 26 83 -69 -52 -93 89 -31 -64 -48 -77 -33 49 -55 -68 60 -23 71 77 45 -61 23 0 75 42 59 -89 69 51 83 -33 -4 81 -66 -67 92 -2 31 74 -18 83 -87 73'.split(' ')
#k = 8
#a = '-97 18 -53 74 93 -48 -30 -59 60 24 -80 -2 80 83 -40 23 57 -31 20 -90 -91 70 -67 -71 43 -99 88 86 -32 -10 -30 -63 -79 49 -51 -64 30 15 -15 81 -34 -87 87 -43 -42 44 39 -63 53 69'.split(' ')

result = angryProfessor(k, a)
print(result)
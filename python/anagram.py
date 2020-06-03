#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    result = []
    r = 0

    for i in range(len(query)): query[i] = ''.join((sorted(query[i])))
    for j in range(len(dictionary)): dictionary[j] = ''.join(sorted(dictionary[j]))

    print(query)
    print(dictionary)

    for i in query:
        for j in dictionary:
            if len(i) == len(j) and i == j: r += 1

        result.append(r)
        r = 0

    return result

# simple case 1
#dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
#query = ['codl', 'heater', 'abcd']

# simple case 2
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
query = ['two', 'bca', 'no', 'listen']


ts1 = time.time()
result = stringAnagram(dictionary, query)
ts2 = time.time()

print(ts2 - ts1)
print('\n'.join(map(str, result)))

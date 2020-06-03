#!/bin/python3

import math
import os
import random
import re
import sys

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

    for i in query:
        q = str(sorted(i))
        for j in dictionary:       
            d = str(sorted(j))
            if q == d: r += 1

        result.append(r)
        r = 0

    return result

# simple case 1
#dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
#query = ['codl', 'heater', 'abcd']

# simple case 2
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
query = ['two', 'bca', 'no', 'listen']

result = stringAnagram(dictionary, query)

print('\n'.join(map(str, result)))

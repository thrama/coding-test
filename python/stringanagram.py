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

    s_query = list(map(lambda s : ''.join((sorted(s))), query))
    s_dictionary = list(map(lambda s : ''.join((sorted(s))), dictionary))

    #print(s_query)
    #print(s_dictionary)

    for i in s_query:
        for j in s_dictionary:
            if i == j: r += 1
            
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

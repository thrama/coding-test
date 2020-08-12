from itertools import groupby

"""
In this task, we would like for you to appreciate the usefulness of the 
groupby() function of itertools. To read more about this function, check 
this out: 
https://docs.python.org/2/library/itertools.html#itertools.groupby

You are given a string S. Suppose a character 'c' occurs consecutively X times 
in the string. Replace these consecutive occurrences of the character 'c' with 
(X, c) in the string. 

Link: https://www.hackerrank.com/challenges/compress-the-string/problem
"""

def compressString(s):
    print(*[(len(list(c)), int(k)) for k, c in groupby(s)])

s = "1222311"
compressString(s)

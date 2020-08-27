#!/usr/local/bin/bash

# There are N integers in an array A. All but one integer occur in pairs. 
# Your task is to find the number that occurs only once.
#
# Link: https://www.hackerrank.com/challenges/lonely-integer-2/problem
#

# read the array from the standard input (ctrl-d to stop the input request)
read 

# tr ' ' '\n' -> translate end-of-line chars in blank chars
# sort -> sort the array
# uniq -u -> extract the unique value
tr ' ' '\n' | sort | uniq -u

# to test...
#echo "1 2 3 3 2" | tr ' ' '\n' | sort | uniq -u

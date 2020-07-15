import math
import os
import random
import re
import sys

#
# HackerLand University has the following grading policy:
# - Every student receives a grades in the inclusive range from 0 to 100.
# - Any grade less than 40 is a failing grade.
#
# Sam is a professor at the university and likes to round each student's grade 
# according to these rules: 
# - If the difference between the grade and the next multiple of 5 is less 
#   than 3, round grade up to the next multiple of 5.
# - If the value of grade is less than 38, no rounding occurs as the result 
#   will still be a failing grade.
#
# For example, grade = 84 will be rounded to 85 but grade 29 will not be 
# rounded because the rounding would result in a number that is less than 40.
# Given the initial value of grade for each of Sam's n students, write code 
# to automate the rounding process. 
#
# Link: https://www.hackerrank.com/challenges/grading/problem
#

def gradingStudents(grades):
    
    r = []
    for i in range(len(grades)):
        if grades[i] < 38:
            r.append(grades[i])
        else:
            if grades[i] % 5 < 3:
                r.append(grades[i])
            else: 
                r.append(grades[i] + (5 - (grades[i] % 5)))

    return r

if __name__ == '__main__':

    # simple test case    
    grades = [ 73, 67, 38, 33 ]

    result = gradingStudents(grades)
    print(result)
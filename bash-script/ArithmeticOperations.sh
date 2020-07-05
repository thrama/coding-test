#!/bin/bash

#
# We provide you with expressions containing +,-,*,^, / and parenthesis. None 
# of the numbers in the expression involved will exceed 999.
#
# Your task is to evaluate the expression and display the correct output 
# rounding upto decimal places. 
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
#

read -p "Enter the expresion to evaluate: " exp

printf "%.3f" $(echo $exp | bc -l)

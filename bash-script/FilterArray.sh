#!/usr/local/bin/bash

#
# We now transition to some basic examples of bash scripting for the purpose 
# of text processing and data munging. In this challenge, we practice reading 
# and filtering an array. 
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns/problem 
#

# sample input
my_array=(Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway)

# filter using regular expression
echo ${my_array[@]/*[aA]*/}

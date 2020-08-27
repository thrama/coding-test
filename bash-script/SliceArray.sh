#!/usr/local/bin/bash

#
# Given a list of countries, each on a new line, your task is to read them 
# into an array. Then slice the array and display only the elements lying 
# between positions 3 and 7, both inclusive. Indexing starts from from 0.
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials-slice-an-array/problem
#

# sample input
my_array=(Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway)

echo ${my_array[@]:3:5}
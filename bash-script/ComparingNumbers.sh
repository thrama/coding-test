#!/bin/bash

#
# Given two integers, X and Y, identify whether X < Y or X > Y or X = Y.
#
# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y 
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem
#

read -p "Enter the first number (X): " x
read -p "Enter the second number (Y): " y

if [ $x -eq $y ]
then
    echo "${x} is equal to ${y}" 
else
    if [ $x -gt $y ]
    then
        echo "${x} is greater than ${y}"
    else
        echo "${x} is less than ${y}"
    fi
fi
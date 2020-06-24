#!/bin/bash

#
# Given two integers, x and y, find their sum, difference, product, and quotient.
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem
#

read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$(( num1 + num2 ))
sub=$(( num1 - num2 ))
molt=$(( num1 * num2 ))
div=$(( num1 / num2 ))
 
echo "$sum"
echo "$sub"
echo "$molt"
echo "$div"   

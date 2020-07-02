#!/bin/bash

#
# Write a Bash script which accepts as input and displays a greeting: 
# "Welcome (name)"
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---a-personalized-echo/problem
#

read -p "Enter your name: " name
echo "Welcome ${name}"
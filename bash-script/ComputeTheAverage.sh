#!/bin/bash

#
# Given N integers, compute their average correct to three decimal places.
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---compute-the-average/problem
#

read -p "Enter total of the numbers (N): " n

sum=0
for ((i=0;i<$n;i++))
do
    read -p "Enter the number ($i): " x
    let "sum+=$x"
done

# this command doesn't work with zsh on macos Catalina
printf "%.3f" $(echo $sum/$n | bc -l)

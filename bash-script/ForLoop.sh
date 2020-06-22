#!/bin/bash

#
# Your task is to use for loops to display only odd natural numbers from 1 to 99.
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem
#

for i in {1..100}
do
	if [ $((i % 2)) != 0 ]; then
		echo "$i"
	fi
done

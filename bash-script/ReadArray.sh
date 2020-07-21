#!/usr/local/bin/bash

#
# Given a list of countries, each on a new line, your task is to read them 
# into an array and then display the entire array, with a space between each 
# of the countries' names. 
#
# Tutorial: https://www.thegeekstuff.com/2010/06/bash-array-tutorial/
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials-read-in-an-array/problem
#

declare -a Vals

# cycling until CTRL+D is pressed
while read p; do
  #echo "$p"
  Vals=("${Vals[@]}" $p)
done

echo ${Vals[@]}
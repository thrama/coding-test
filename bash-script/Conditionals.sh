#!/bin/bash

#
# Read in one character from the user (this may be 'Y', 'y', 'N', 'n'). If the 
# character is 'Y' or 'y' display "YES". If the character is 'N' or 'n' 
# display "NO". No other character will be provided as input. 
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem
#

read -p "Enter Y or N: " char

if [[ $char == "Y" || $char == "y" ]];
then 
    echo "YES"
else
    if [[ $char == "N" || $char == "n" ]];
    then 
        echo "NO"
    else
        ECHO "Invalid character"
    fi
fi
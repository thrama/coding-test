#!/bin/bash

#
# Given three integers (X, Y, and Z) representing the three sides of a 
# triangle, identify whether the triangle is Scalene, Isosceles, or 
# Equilateral.
#
# Link: https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem
#

read -p "Enter X: " x
read -p "Enter Y: " y
read -p "Enter Z: " z

if [ $x -eq $y ];
    then
        if [ $y -eq $z ];
            then
                # EQUILATERAL
                echo "EQUILATERAL"
            else 
                # ISOSCELES
                echo "ISOSCELES"
        fi
    else
        if [ $y -eq $z ];
            then
                # ISOSCELES
                echo "ISOSCELES"
            else 
                # SCALENE
                echo "SCALENE"
        fi
fi

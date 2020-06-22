import sys

"""
Given an array, a, of size n distinct elements, sort the array in ascending 
order using the Bubble Sort algorithm above. Once sorted, print the following
3 lines:

1. 'Array is sorted in numSwaps swaps.'
    where numSwaps is the number of swaps that took place.
2. 'First Element: firstElement'
    where firstElement is the first element in the sorted array.
3. 'Last Element: lastElement'
    where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps 
a running tally of all swaps that occur during execution. 

Link: https://www.hackerrank.com/challenges/30-sorting/problem
"""

def swapPositions(list, pos1, pos2):      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

# sample input 1
n = 3
a = [3, 2, 1]

numberOfSwaps = 0
for i in range(n): 
    # track number of elements swapped during a single array traversal
    
    for j in range(n - 1):
        # swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            swapPositions(a, j, j + 1)
            numberOfSwaps += 1
        
    # if no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0):
        break

print(f'Array: {a}')

# output:
print(f'Array is sorted in {numberOfSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')
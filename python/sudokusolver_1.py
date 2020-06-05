import sys
import numpy as np

def possible(y,x,n):
    '''
    Check if n is a correct value for the position y,n in the grid
    '''
    global grid

    # check the row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # check the column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # check the box
    x0, y0 = (x//3)*3, (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False

    return True

def solve():
    '''
    Try to solve the Sudoku with a backtracking/recursive approach
    '''
    global grid

    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] == n
                        solve()
                        # if the recursion get back it means the solution find isn't correct, so it set the value back to 0
                        grid[y][x] == 0
                return

    print(np.matrix(grid))
    input("more?")


'''
grid = [[5,1,7,6,0,0,0,3,4],
        [2,8,9,0,0,4,0,0,0],
        [3,4,6,2,0,5,0,9,0],
        [6,0,2,0,0,0,0,1,0],
        [0,3,8,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]
'''
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

solve()


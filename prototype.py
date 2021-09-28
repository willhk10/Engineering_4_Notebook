#  Python Sudoku Solver
#  Made by William Keenan
#  9/28/21

from pprint import pprint   #Can be used to print more complicated data structures

def find_next_value(puzzle): 
    for r in range(9):
        if puzzle[r][c] = 0
        return r, c #This is essentially defining the row and column that the program will be attempting to solve for

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in puzzle[row]: # This function defines what if the guess is currently defined in the row of the value being altered.
        return False
    col_vals = [puzzle[a][col] for i in range(9)] # This is checking all column values at the specified location in the current column
    if guess in col_vals:
        return False
    
def solveSudoku(puzzle):
    row, col = find_next_value
    
    if is_valid True:
        

puzzle = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
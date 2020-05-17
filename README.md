# sudoku-solver-python

This is a sudoku solver I created in 2015-2016. It check subsquares, virtical and horizontal lines, then runs swordfish technique over to solve. 

## How to run
1. Set your puzzle
    Edit the **setPuzzle** function with your unsolved sudoku puzzle.
    ```python
    #Set your puzzle here.
    def setPuzzle():
        puzzle = [[' ',' ',' ','9','1','3','7',' ',' '],
                  [' ','2',' ',' ','8',' ',' ','1',' '],
                  ['1',' ','9',' ','5',' ','3',' ',' '],
                  [' ','1',' ','7','2',' ',' ','4','3'],
                  [' ','3',' ','8',' ',' ',' ','5',' '],
                  [' ',' ',' ',' ','4',' ',' ','7',' '],
                  ['6','5',' ',' ',' ',' ',' ','3',' '],
                  ['7',' ','3',' ',' ',' ','8',' ',' '],
                  ['2','9',' ',' ',' ','8',' ',' ',' ']]
        return puzzle
    ```
2. Run
    ```bash
    python sudoku.py
    ```
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

#easy
# def setPuzzle():
#     puzzle = [[' ','9',' ',' ',' ','4',' ','1',' '],
#               ['2',' ','4',' ',' ','8','9','6',' '],
#               [' ',' ',' ',' ','9',' ','4',' ','7'],
#               [' ',' ',' ',' ',' ',' ','3','8','9'],
#               [' ',' ','9','6',' ','7','1',' ',' '],
#               ['1','4','3',' ',' ',' ',' ',' ',' '],
#               ['9',' ','2',' ','7',' ',' ',' ',' '],
#               [' ','1','5','9',' ',' ','7',' ','6'],
#               [' ','6',' ','1',' ',' ',' ','9',' ']]
#     return puzzle

#hard
# def setPuzzle():
#     puzzle = [['8',' ',' ',' ',' ',' ',' ',' ',' '],
#               [' ',' ','3','6',' ',' ',' ',' ',' '],
#               [' ','7',' ',' ','9',' ','2',' ',' '],
#               [' ','5',' ',' ',' ','7',' ',' ',' '],
#               [' ',' ',' ',' ','4','5','7',' ',' '],
#               [' ',' ',' ','1',' ',' ',' ','3',' '],
#               [' ',' ','1',' ',' ',' ',' ','6','8'],
#               [' ',' ','8','5',' ',' ',' ','1',' '],
#               [' ','9',' ',' ',' ',' ','4',' ',' ']]
#     return puzzle

#initialise variables
candidatePuzzle =[[[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[],[]],]
array = ['1','2','3','4','5','6','7','8','9']
container = [[],[],[],[],[],[],[],[],[]]
marker = []
lookup = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}
square = True
vLine = True
hLine = True

#Returns False if x is already in the row of the puzzle.
def notInRow(x,row, puzzle):
    for c in range(9):
        if puzzle[row][c] == x:
            return False
    return True

#Return False if x is already in column of the puzzle
def notInColumn(x, col, puzzle):
    for r in range(9):
        if puzzle[r][col] == x:
            return False
    return True

#Returns False if x is in the square that it resides in the puzzle
#row and column are between 0-8! (not 1-9)
def notInSquare(x, row, col, puzzle):
    if row <3 and col <3:
        #left top
        for a in range(3):
            for b in range(3):
                if puzzle[a][b] == x:
                    return False
    elif row >2 and row <6 and col <3:
        #left middle
        for a in range(3,6):
            for b in range(3):
                if puzzle[a][b] == x:
                    return False
    elif row >5 and col <3:
        #left bottom
        for a in range(6,9):
            for b in range(3):
                if puzzle[a][b] == x:
                    return False
    elif row <3 and col >2 and col <6:
        #middle top
        for a in range(3):
            for b in range(3,6):
                if puzzle[a][b] == x:
                    return False
    elif row >2 and row <6 and col >2 and col <6:
        #middle middle
        for a in range(3,6):
            for b in range(3,6):
                if puzzle[a][b] == x:
                    return False
    elif row >5 and col >2 and col <6:
        #middle bottom
        for a in range(6,9):
            for b in range(3,6):
                if puzzle[a][b] == x:
                    return False
    elif row <3 and col >5:
        #right top
        for a in range(3):
            for b in range(6,9):
                if puzzle[a][b] == x:
                    return False
    elif row >2 and row <6 and col >5:
        #right middle
        for a in range(3,6):
            for b in range(6,9):
                if puzzle[a][b] == x:
                   return False
    elif row >5 and col >5:
        #right bottom
        for a in range(6,9):
            for b in range(6,9):
                if puzzle[a][b] == x:
                    return False
    return True

#checks if the Sudoku puzzle is all filled in
def checkSudoku(puzzle):
    for row in puzzle:
        for col in row:
            if col == ' ':
                return False
    return True

#prints Sudoku, taking the a string header and the puzzle to print
def printSudoku(string, puzzle):
    print(string)
    for r in range(9):
        print(puzzle[r])
    print(" ")

#If there is only 1 candidate for a unit, then apply that candidate to puzzle
def applyanalyse(candidatePuzzle, puzzle):
    for r in range(9):
        for c in range(9):
            if len(candidatePuzzle[r][c]) == 1:
                puzzle[r][c] = candidatePuzzle[r][c][0]

#Stores all candidate numbers in an array for that unit.
def analyseCandidateReduction(puzzle):
    candidatePuzzle =[[[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],
                 [[],[],[],[],[],[],[],[],[]],]
    for x in array:
        for r in range(9):
            if notInRow(x,r,puzzle): #if not in row..
                for c in range(9):
                    if(puzzle[r][c] == ' '): #if empty..
                        if notInColumn(x,c,puzzle): #if not in column..
                            if notInSquare(x,r,c,puzzle): #if not in its square..
                                candidatePuzzle[r][c] += x
    applyanalyse(candidatePuzzle, puzzle)
    return candidatePuzzle

#Analyse for commen items in their squares. Container
def analyseCommonSquare(puzzle):
    container = [[],[],[],[],[],[],[],[],[]]
    marker = []
    for k in range(2):
        i = 0
        #left top
        for a in range(3):
            for b in range(3):
                appendContainer(container,marker,a,b,i,k)
        #left middle
        i+=1
        for a in range(3,6):
            for b in range(3):
                appendContainer(container,marker,a,b,i,k)
        #left bottom
        i+=1
        for a in range(6,9):
            for b in range(3):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #middle top
        for a in range(3):
            for b in range(3,6):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #middle middle
        for a in range(3,6):
            for b in range(3,6):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #middle bottom
        for a in range(6,9):
            for b in range(3,6):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #right top
        for a in range(3):
            for b in range(6,9):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #right middle
        for a in range(3,6):
            for b in range(6,9):
                appendContainer(container,marker,a,b,i,k)
        i+=1
        #right bottom
        for a in range(6,9):
            for b in range(6,9):
                appendContainer(container,marker,a,b,i,k)
        #now find single numbers in arrays for each sqare
        if k == 0:
            for row in container:
                for x in array:
                    if(row.count(x)== 1):
                        print("MARKED FOUND: ", x)
                        marker.append(x)
                    else:
                        marker.append('0')
    return marker

def appendContainer(cotainer,marker,a,b,i,k):
    if len(candidatePuzzle[a][b]) > 1:
        for item in candidatePuzzle[a][b]:
            if k == 0:
                container[i].append(item)
            else:
                if item == marker[i]:
                    puzzle[a][b] = marker[i]

def analyseCommonVLine(puzzle):
    container = [[],[],[],[],[],[],[],[],[]]
    marker = []
    for i in range(2):
        for r in range(9):
            for c in range(9):
                for item in candidatePuzzle[r][c]:
                    container[r].append(item)
                    if i ==1:
                        if item == marker[r]:
                            puzzle[r][c] = marker[r]
        if i == 0:
            m = 0
            for row in container:
                for x in array:
                    found = False
                    if(row.count(x)== 1):
                        marker.append(x)
                        found = True
                        break
                if found == False:
                    marker.append('0')
                m+=1
    return marker

def analyseCommonHLine(puzzle):
    container = [[],[],[],[],[],[],[],[],[]]
    marker = []
    for i in range(2):
        for r in range(9):
            for c in range(9):
                for item in candidatePuzzle[c][r]:
                    container[r].append(item)
                    if i ==1:
                        if item == marker[r]:
                            puzzle[c][r] = marker[r]
        if i == 0:
            for col in container:
                for x in array:
                    found = False
                    if(col.count(x)== 1):
                        marker.append(x)
                        found = True
                        break
                if found == False:
                    marker.append('0')
    return marker

def markerSuccess(marker):
    for r in range(len(marker)):
        if marker[r] != '0':
            return True
    return False


def swordfishCheck():
    swordfishArray = [[],[],[],[],[],[],[],[],[]]
    tempArray = [[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[],],[[],[]],[[],[]],[[],[]]]
    for r in range(9): #place candidate cooridinates into swordfishArray
        for c in range(9):
            for item in candidatePuzzle[r][c]:
                for i in range(9):
                    if item == array[i]:
                        swordfishArray[i].append([r,c])
    for c in range(len(swordfishArray)): #seperate cooridinates of swordfishArray into temp array ^could be done in above loop
        for item in swordfishArray[c]:
            tempArray[c][0].append(item[0])
            tempArray[c][1].append(item[1])
    escape = False
    for i in range(9):
        if len(tempArray[i][0]) == 0:
            continue
        for l in range(9):# pair items, if there are less or more than 2 of a number, then it is not valid for swordfishing
            for m in range(2):
                if tempArray[i][m].count(l) == 2:
                    lookup[array[i]] = True
                    continue
                elif tempArray[i][m].count(l) == 0: #not in list, its ok
                    continue
                else:
                    lookup[array[i]] = False
                    escape = True
                    break
            if escape == True:
                escape = False
                break

def applySwordfish(x, puzzle):
    for r in range(9):
        for c in range(9):
            if len(candidatePuzzle[r][c]) > 2:
                continue      #swordfish won't risk brute force if there are more than 2 candidates
            for item in candidatePuzzle[r][c]:
                if item == x:
                    puzzle[r][c] = x
                    return puzzle



puzzle = setPuzzle()
printSudoku("original problem", puzzle)
#analyse using candidate reduction
while(square or vLine or hLine): #while there was still changes being made
    candidatePuzzle = analyseCandidateReduction(puzzle)
    square = markerSuccess(analyseCommonSquare(puzzle))
    vLine = markerSuccess(analyseCommonVLine(puzzle))
    hLine = markerSuccess(analyseCommonHLine(puzzle))

printSudoku("candidate checked:", puzzle)
if not checkSudoku(puzzle):#if still not completed, swordfish.
    print("Still not completed: Swordfishing.")
    swordfishCheck()
    for item in lookup:
        backupPuzzle = puzzle
        if lookup[item] == True:
            #reset variables for analyse
            square = True
            vLine = True
            hLine = True
            backupPuzzle = applySwordfish(item, backupPuzzle)
            printSudoku("Swordfished: ", backupPuzzle)
            while(square or vLine or hLine):
                candidatePuzzle = analyseCandidateReduction(backupPuzzle)
                square = markerSuccess(analyseCommonSquare(backupPuzzle))
                vLine = markerSuccess(analyseCommonVLine(backupPuzzle))
                hLine = markerSuccess(analyseCommonHLine(backupPuzzle))
            if checkSudoku(backupPuzzle):
                break
    puzzle = backupPuzzle
printSudoku("results:" , puzzle)

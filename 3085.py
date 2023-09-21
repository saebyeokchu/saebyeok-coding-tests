'''

4
PPPP
CYZY
CCPY
PPCC

'''
import numpy

def checkRight(board, row, col, boardLen, longestResult) :
    tempLogestResult = longestResult
    
    #swap value
    left = board[row][col]
    right = board[row][col+1]
    
    board[row][col] = right
    board[row][col+1] = left
    
    startValue = left
    count = 1
    
    print("====board[{}][{}]오른쪽체크=====".format(row,col))
    print(board)
    
    #해당 row의 가로 체크
    for i in range(0,boardLen-1) :
        if board[row][i] == startValue and board[row][i] == board[row][i+1] :
            count = count + 1
            
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("가로체크 ===> logest result : ",longestResult,", count : ",count)
    
    count = 1
    
    #해당 col의 세로 체크
    for i in range(0,boardLen-1) :
        if board[i][col] == startValue and board[i][col] == board[i+1][col] :
            count = count + 1
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("세로체크 ===> logest result : ",tempLogestResult,", count : ",count)
        
    board[row][col] = left
    board[row][col+1] = right
    
    return tempLogestResult

def checkLeft(board, row, col, boardLen, longestResult) :
    tempLogestResult = longestResult
    
    #swap value
    left = board[row][col-1]
    right = board[row][col]
    
    board[row][col-1] = right
    board[row][col] = left
    
    startValue = right
    count = 1
    
    print("====board[{}][{}]왼쪽체크=====".format(row,col))
    print(board)
    
    #해당 row의 가로 체크
    for i in range(0,boardLen-1) :
        if board[row][i] == startValue and board[row][i] == board[row][i+1] :
            count = count + 1
            
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("가로체크 ===> logest result : ",longestResult,", count : ",count)
    
    count = 1
    
    #해당 col의 세로 체크
    for i in range(0,boardLen-1) :
        if board[i][col] == startValue and board[i][col] == board[i+1][col] :
            count = count + 1
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("세로체크 ===> logest result : ",tempLogestResult,", count : ",count)
        
    board[row][col-1] = left
    board[row][col] = right
    
    return tempLogestResult

def checkTop(board, row, col, boardLen, longestResult) :
    tempLogestResult = longestResult
    
    #swap value
    top = board[row-1][col]
    bottom = board[row][col]
    
    board[row-1][col] = bottom
    board[row][col] = top
    
    startValue = bottom
    count = 1
    
    print("====board[{}][{}]위쪽체크=====".format(row,col))
    print(board)
    
    #해당 row의 가로 체크
    for i in range(0,boardLen-1) :
        if board[row][i] == startValue and board[row][i] == board[row][i+1] :
            count = count + 1
            
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("가로체크 ===> logest result : ",longestResult,", count : ",count)
    
    count = 1
    
    #해당 col의 세로 체크
    for i in range(0,boardLen-1) :
        if board[i][col] == startValue and board[i][col] == board[i+1][col] :
            count = count + 1
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("세로체크 ===> logest result : ",tempLogestResult,", count : ",count)
        
    board[row][col-1] = top
    board[row][col] = bottom
    
    return tempLogestResult
    
def checkBottom(board, row, col, boardLen, longestResult) :
    tempLogestResult = longestResult
    
    #swap value
    top = board[row][col]
    bottom = board[row+1][col]
    
    board[row][col] = bottom
    board[row+1][col] = top
    
    startValue = top
    count = 1
    
    print("====board[{}][{}]아래쪽체크=====".format(row,col))
    print(board)
    
    #해당 row의 가로 체크
    for i in range(0,boardLen-1) :
        if board[row][i] == startValue and board[row][i] == board[row][i+1] :
            count = count + 1
            
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("가로체크 ===> logest result : ",longestResult,", count : ",count)
    
    count = 1
    
    #해당 col의 세로 체크
    for i in range(0,boardLen-1) :
        if board[i][col] == startValue and board[i][col] == board[i+1][col] :
            count = count + 1
    
    if count > 1 and count > longestResult:
        tempLogestResult = count
    
    print("세로체크 ===> logest result : ",tempLogestResult,", count : ",count)
        
    board[row][col] = top
    board[row+1][col] = bottom
    
    return tempLogestResult    
    
boardLen = 4
inputs_ = ''

for i in range(0,boardLen) :
    inputs_ = inputs_ + input()
board = numpy.full((boardLen,boardLen), ' ')
longestResult = 0;

#initial setting
for row in range(0,boardLen) :
    for col in range(0,boardLen) :
        board[row][col] = inputs_[row*3+col]
 
#check one by one
for row in range(0,boardLen) :
    for col in range(0,boardLen) :
        #check right
        #check if right value exist
        if col + 1 != boardLen :
            longestResult = checkRight(board, row, col, boardLen, longestResult)
            if longestResult == boardLen :
                break;
            print("\n\n")
        
        #check left
        if col - 1 >= 0 :
            longestResult = checkLeft(board, row, col, boardLen, longestResult)
            if longestResult == boardLen :
                break;
            print("\n\n")
            
        #check top
        if row - 1 >= 0 :
            longestResult = checkTop(board, row, col, boardLen, longestResult)
            if longestResult == boardLen :
                break;
            print("\n\n")
        
        #check bottom
        if row + 1 != boardLen :
            longestResult = checkBottom(board, row, col, boardLen, longestResult)
            if longestResult == boardLen :
                break;
            print("\n\n")
print(longestResult)









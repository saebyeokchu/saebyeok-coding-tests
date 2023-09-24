import math

#check 연속성
def checkContinuity(board, longestResult, checkRow, checkCol) :
    max_cnt = 1
    
    for i in range(N) :
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt
    
def swap(board,targetRow,targetCol,sourceRow,sourceCol) :
    temp = board[targetRow][targetCol];
    board[targetRow][targetCol] = board[sourceRow][sourceCol]
    board[sourceRow][sourceCol] = temp

def check(board, row, col, boardLen, ans, direc) :
    
    targetRow = row + direc[0]
    targetCol = col + direc[1]
    
    if targetRow < 0 or targetRow >= boardLen :
        return ans
    
    if targetCol < 0 or targetCol >= boardLen :
        return ans
    
    swap(board, row, col, targetRow, targetCol)
    result = checkContinuity(board, ans, row, col)
    swap(board, row, col, targetRow,targetCol)
    
    return max(result,ans)
    
N = int(input())
board = [list(input()) for _ in range(N)]
ans = 0

direction = [
    [0,1], #오른쪽
    [1,0], #아래쪽
]
    

#check one by one
for row in range(0,N) :
    for col in range(0,N) :
        for direc in direction :
            ans = check(board, row, col, N, ans, direc)
            if ans == N :
                break

                
print(ans)

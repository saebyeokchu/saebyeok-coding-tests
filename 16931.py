N, M = map(int, input().split()) #세로, 가로
L = [list(map(int, input().split())) for _ in range(N)]

Above, Below, front, Back, Right, Left = N*M, N*M, 0, 0, 0, 0


for i in range(N) :
    for j in range(M) :
        if j == 0 :
            Right += L[i][j]
        elif L[i][j-1] < L[i][j] :
            Right += L[i][j] - L[i][j-1]



for j in range(M) :
    for i in range(N) :
        if i == 0 :
            front += L[i][j]
        elif L[i-1][j] < L[i][j] :
            front += L[i][j] - L[i-1][j]
            
print(2*(Right + front+ Below))

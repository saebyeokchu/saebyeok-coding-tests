from collections import deque

N, M = map(int, input().split(' '))
K = [list(map(str, input())) for _ in range(N)]

direction = [[1,0],[0,1],[0,-1],[-1, 0]]
sheepCount = 0
wolfCount = 0

def checkIfSheepOrWolf(val,animals) : 
    if val == 'k' :
        animals[0] += 1
    if val == 'v' :
        animals[1] += 1

            
for x in range(N) :
    for y in range(M) :
        if K[x][y] != '#':
            queue = deque()
            animals = [0,0]
            queue.append([x,y])
            checkIfSheepOrWolf(K[x][y],animals)
            K[x][y]='#'
            
            while queue :
                currentX, currentY = queue.popleft()
                
                for d in direction :
                    nextX = currentX + d[0]
                    nextY = currentY + d[1]
                    
                    if 0 <= nextX < N and 0 <= nextY < M :
                        if K[nextX][nextY] != '#':
                            queue.append([nextX,nextY])
                            checkIfSheepOrWolf(K[nextX][nextY],animals)                           
                            K[nextX][nextY]='#'
            if animals[0] > animals[1] :
                sheepCount += animals[0]
            else :
                wolfCount += animals[1]
                            
print(sheepCount,wolfCount)
            

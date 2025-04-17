N = int(input())
M = [list(map(int, input())) for _ in range(N)]
visited = [[0 for j in range(N)] for i in range(N)]
ans = []

direction = [[1,0],[0,1],[0,-1],[-1, 0]]

for i in range(N) :
    for j in range(N) :
        queue = []
        if M[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            queue.append([i,j])
            count = 1
            
            while len(queue) > 0 :
                item = queue.pop(0)
                
                currentX = item[0]
                currentY = item[1]
                
                for direct in direction :
                    
                    nextX = currentX + direct[0]
                    nextY = currentY + direct[1]
                    
                    if 0 <= nextX < N and  0 <= nextY < N :
                    
                        if M[nextX][nextY] == 1 and  visited[nextX][nextY] == 0 :
                            count += 1
                            visited[nextX][nextY] = 1
                            queue.append([nextX,nextY])
            if count > 0 :
                ans.append(count)

ans.sort()
print(len(ans))
print(*ans,sep="\n")

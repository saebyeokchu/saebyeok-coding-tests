from collections import deque 

N, M = map(int,input().split())

visited = [0]*1000001

queue = deque()
queue.append([N])
visited[N] = 1

#더하기 일, 빼기 일, 곱하기 2
while queue :
    vals = queue.popleft()
    lastElement = vals[len(vals)-1]
    
    
    if lastElement == M :
        print(len(vals)-1)
        print(*vals)
        break
    
    for v in [lastElement+1,lastElement-1,lastElement*2] :
        if 0<= v <= 1000000 and visited[v] == 0 :
            temp = vals.copy()
            temp.append(v)
            queue.append(temp)
            visited[v] = 1

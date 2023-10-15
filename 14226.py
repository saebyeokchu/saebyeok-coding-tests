#while True :
S=int(input())
MAX = 2001
clipboard = [0] * MAX
visited = [0] * MAX
parent = [0] * MAX

queue = []
queue.append(1)
parent[1] = 1
visited[1] = 1
clipboard[1] = 1

while len(queue) > 0 :
    q = queue.pop(0)
    visited[q] = 1
    if q == S :
        break
    
    #남의 클립보드를 함께 안써야 한다
    for c in [clipboard[q], q] :
        if  1<= q+c <= MAX and visited[q+c] == 0 :
            queue.append(q+c)
            if c == q :
                visited[q+c] = 2
            else :
                visited[q+c] = 1
            parent[q+c] = q
            clipboard[q+c] = c
        
    if 1 <= q - 1 <= MAX and visited[q-1] == 0 :
        queue.append(q-1)
        visited[q-1] = 1
        parent[q-1] = q
        clipboard[q-1] = clipboard[q]      
    

dest = S
count = 0
while dest > 1 :
    #print(dest,":",visited[dest])
    count += visited[dest]
    dest = parent[dest]

print(count)

S=6
count = [0] * (S+1)
visited = [0] * (S+1)
clipboard = []

queue = []
queue.append(1)

while len(queue) > 0 :
    q = queue.pop(0)
    if q == S :
        break
        
    clipboard.append(q)
    count[q] += 1
    
    for c in clipboard :
        if q+c <= S and visited[q+c] == 0 :
            queue.append(q+c)
            count[q+c] += 1
            visited[q+c] = 1
        
    for k in queue :
        if k - 1 > q and visited[k] == 0 :
            queue.append(k-1)
            count[k-1] += 1
    
    print(q,"======>",queue, "\n")

print(count)

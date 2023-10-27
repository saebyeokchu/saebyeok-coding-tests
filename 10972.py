N = int(input())
L = "".join(list(input().split(" ")))
R = []

def bfs(queue) :
    while len(queue) > 0 :
        p = queue.pop(0)
        
        if len(p) == N :
            R.append(p) 

        else : 
            for j in range(1, N+1) :
                if p.find(str(j)) == -1 :
                    queue.append(p+str(j))
                    
for i in range(int(L[0]),N+1) :
    queue = []
    queue.append(str(i))
    
    bfs(queue)

print(R[R.index(L)+1] if R.index(L) != len(R) - 1 else -1)

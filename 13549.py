#same level
import time
import sys

input_ = sys.stdin.readline()
k, M = map(int,input_.split(" "))
start = time.time()
time_ = [0] * 100001
visited_ = [0] * 100001
queue = []

def bfs(val) :
    global visited_
    queue.append(val)
    
    while len(queue) > 0 :
        n = queue.pop(0)
       
        if n == M :
            print(time_[M])
            return
        
        for v in [n+1, n-1, n*2] :
            if 0 < v < 100001 and visited_[v] == 0 :
                if v == n*2 :
                    time_[v] = time_[n]
                else :
                    time_[v] = time_[n] + 1 
                visited_[v] = 1
                queue.append(v)
bfs(k)

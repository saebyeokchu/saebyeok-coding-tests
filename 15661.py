import math

N = int(input())
M = [ list(map(int,input().split(" "))) for _ in range(N) ]

result = []
min_ = float("inf")

def cal(arr) :
    sum_ = 0
    
    for i in range(len(arr)-1) :
        for j in range(i+1,len(arr)) :
            sum_ += M[arr[i]-1][arr[j]-1] + M[arr[j]-1][arr[i]-1]
    return sum_

            
            
def sol(idx, depth) :
    global min_
 
    if depth == 0 :
        opposite = []
    
        #opposite array 만들기
        for i in range(N) :
            if i+1 not in result :
                opposite.append(i+1)
                
        min_ = min(min_,abs(cal(result)-cal(opposite)))
  
    for i in range(idx+1,N+1) :
        result.append(i)
        sol(i, depth-1)
        result.pop()
    
    
for i in range(2,math.floor(N/2)+1) :
    sol(0,i)

print(min_)

    

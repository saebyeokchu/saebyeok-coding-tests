N = 4
M = [
        [0,1,2,3,4,5],
        [1,0,2,3,4,5],
        [1,2,0,3,4,5],
        [1,2,3,0,4,5],
        [1,2,3,4,0,5],
        [1,2,3,4,5,0]
    ]

result = []

def sol(idx, depth) :
 
    if depth == 0 :
        print(*result)
  
    for i in range(idx+1,7) :
        result.append(i)
        sol(i, depth-1)
        result.pop()
        
    
   
    
for i in range(2,5) :
    print("comb ",i)
    sol(0,i)

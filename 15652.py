N, M = map(int, input().split(" "))

result = []

def sol(start) :
    
    if len(result) == M :
        print(*result)
        return
    
    for i in range(start,N) :
        result.append(i+1)
        sol(i)
        result.pop()
    

sol(0)

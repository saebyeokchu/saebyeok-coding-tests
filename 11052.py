from collections import deque

N = 4
M= [1, 5, 6, 7] #1,2,3,4번의 카드가 있음

d = [0] * (len(M)+1)

result =[]
def sol(val) :
    global result
    
    if val == N :
        print(*result)
        #result=[]
        return
    
    for i in range(1,len(M)+1) :
        if val + i <= N :
            result.append(i)
            sol(val+i)
    

for i in range(1,len(M)+1):
    print("=============>",i)
    result.append(i)
    sol(i)

print("d =====> ", d)

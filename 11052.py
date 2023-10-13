from collections import deque

N = 4
M= [0,1, 5, 6, 7] #1,2,3,4번의 카드가 있음

d = [0] * (len(M))
max_ = 0

def sol(val,sum_) :
    global max_
    if val == N :
        print(sum_)
        max_ = max(max_,sum_)
        return
    
    for i in range(1,len(M)) :
        if val + i <= N :
            result.append(i)
            sol(val+i,sum_ + M[i])
    

for i in range(1,len(M)):
    print("=============>",i)
    result.append(i)
    sol(i,M[i])

print(max_)

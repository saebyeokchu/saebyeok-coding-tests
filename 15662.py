N = int(input())
L = [list(map(int,input())) for _ in range(N)]

#2번의 ACTION
A = int(input())
AD = []

for _ in range(A) :
    AD.append(list(map(int,input().split(" "))))
queue = []

def clockWise(gear) :
    right = gear[-1:]
    left = gear[:-1]
    
    return right + left

def counterColckWise(gear) :
    right = gear[1:]
    left = gear[:1]
    
    return right + left

queue = []

for ad in AD :
    v = [0] * N
    queue = [ad]

    while len(queue) > 0 :
        q = queue.pop(0)
            
        gearIndex = q[0] - 1
        goTo = q[1]
    
        v[gearIndex] = 1
        
        leftTouchVal = L[gearIndex][6]
        rightTouchVal = L[gearIndex][2]
        
        #첫번째 톱니바퀴를 오른쪽으로 1회회전
        L[gearIndex] =  clockWise(L[gearIndex]) if goTo == 1 else counterColckWise(L[gearIndex])
    
        #왼쪽, 오른쪽 톱니 바퀴 번호
        leftGearIndex = gearIndex - 1
        rightGearIndex = gearIndex + 1
        
        if leftGearIndex >= 0 and leftGearIndex < len(L) and v[leftGearIndex] == 0:
            if L[leftGearIndex][2] != leftTouchVal :
                queue.append([leftGearIndex+1, goTo*(-1)])
                    
        if rightGearIndex >= 0 and rightGearIndex < len(L) and v[rightGearIndex] == 0:
            if rightTouchVal != L[rightGearIndex][6] :
                queue.append([rightGearIndex+1, goTo*(-1)])

count = 0
for l in L :
    if l[0] == 1 :
        count += 1
        
print(count)

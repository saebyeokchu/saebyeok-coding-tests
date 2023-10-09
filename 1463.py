#2가 1이 되는 최선의 방법

D = [0]*((10 ** 6) + 1)

def check(vals) :
    returnArr = []
    
    for val in vals :
        if val%3 == 0 and int(val/3) >= 1:
            returnArr.append(int(val / 3))
        
        if val%2 == 0 and int(val/2) >= 1 :
            returnArr.append(int(val / 2))
        
        if val-1 >= 1 :
            returnArr.append(val-1)
    
    return returnArr

M = int(input())

for N in range(2,M+1):
    vals = [N]
    checked = False
    count = 0
    while len(vals) > 0 :
        
        count += 1
        vals = check(vals)
        
        for val in vals :
            if D[val] != 0 :
                checked = True
                D[N] = min(D[N], D[val] + count) if D[N] != 0 else  D[val] + count
        
            if val == 1 :
                checked = True
                D[N] = min(D[N], count) if D[N] != 0 else count
        
        if checked :
            break

print(D[M])


n = 5
p=[0] + [10,9,8,7,6]
d = [0] * (n+1)

d[n] = p[n]

def find(chase, total):
    
    if chase == n :
        print("total : " , total)
        return
    
    print("chase : " , chase)
    
    for i in range(1, n+1) :
        if chase + i <= n :
            if d[chase+i] == 0 :
                d[chase+i] = total + p[i]
            elif d[chase+i] > total + p[i]:
                d[chase+i] = total + p[i]
            find(chase+i, total + p[i])

for i in range(1, n+1) :
    find(i, p[i])

print(d)

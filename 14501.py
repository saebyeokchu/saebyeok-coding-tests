n=int(input())
t = [0] * ( n  )
p = [0] * ( n  )
d=[0]* ( n + 1 )

for i in range(0,n) :
    t[i],p[i] = map(int,input().split(" "))

for i in range(n-1,-1,-1) :
    if t[i] + i > n:
        d[i] = d[i+1]
    else :
        d[i] += max(d[i+1],d[i+t[i]] + p[i])

print(d[0])

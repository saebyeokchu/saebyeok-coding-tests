n = 12
d = [0] * (n+1)

d[1] = 1
d[2] = 3

for j in range(3,n+1) :
    ans = 0
    for i in range(j-1,0,-1) :
        ans += d[i] * d[j-i]
        #print(i," : ",j-i," => ", d[i] * d[j-i])
    d[j] = ans - (j-2) 
    print(j,"=>",d[j],":",( d[j] % 10007) )

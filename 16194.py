n = 4
p=[0] + [3,5,15,16]
d = [0] * (n+1)

d[n] = p[n]

def find():

for i in range(1, n) :
    find(0, i)
        

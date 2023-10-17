n=0

l,m,z = map(int,input().split(" "))

while True:
    sun = 28*n + m
    checksun = (sun - l) % 15 == 0
    checkmoon = (sun - z) % 19 == 0

    if checksun and checkmoon :
        print(sun)
        break
            
    n += 1

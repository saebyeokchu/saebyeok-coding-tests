import sys

maxNum = 1000000

primes = list(range(maxNum + 1))
issqt = int(maxNum**0.5) + 1

for i in range(2, issqt) :
    if primes[i] :
        primes[i+i::i] = [0] * len(primes[i+i::i])

while True :
    m0 = int(sys.stdin.readline())
    
    if m0 == 0 :
        break
    
    for m1 in range(3, int(m0 / 2) + 1, 2) :
        if primes[m1] and primes[m0 - m1] :
            print(f"{m0} = {m1} + {m0 - m1}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')

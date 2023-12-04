
def isPrime(n) :
    for i in range(2, int(n**0.5) +1 ) :
        if n % i == 0 :
            return False
    return True
    
while True :
    m0 = int(input())
    
    if m0 == 0 :
        break
    
    m1 = 2
    while m1 > 1 :
        if isPrime(m1) :
            m2 = m0 - m1
            if isPrime(m2):
                print(f"{m0} = {m1} + {m2}")
                break
        m1 += 1

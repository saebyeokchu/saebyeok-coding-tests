# 2-> 4
#10 -> 87
import time

#약수의 합의 합
divisor = [0] * 100001
sumOfDivs = [0] * 100001
divisor[1] = 1
divisor[2] = 3
divisor[3] = 4


#dynamic programming -> save previous results
#fast wat to get 약수

#56의 약수 1 2 4 7 8 14 28 56

def find_sum(inputs) :
    num = int(inputs)


#find divisior
def find_divisor(inputs) :
    num = int(inputs)
    if divisor[num] != 0 :
        return divisor[num]

    else :
        for i in range(1,num//2):
            if num % i == 0 :
                divisor[num] += i
                divisor[num] += num // i
        return divisor[num]

while True :
    sumOfDivs = 0
    num = int(input())
    start = time.time()
    for i in range(1, num + 1) :
        sumOfDivs += find_divisor(i)
    end = time.time()
    
    print(sumOfDivs, end-start)

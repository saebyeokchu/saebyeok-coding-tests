import sys
import math

C = int(input())

for j in range(0, C) :
    N = int(input())
    M = list(map(int,input().split()))
    visited = [0] * len(M)
    M.sort()
    
    oddList = M[0::2]
    evenList = M[1::2]
    oddMin = -sys.maxsize
    #oddList에서 최대값
    for i in range(1, len(oddList) ) :
        diff = oddList[i] - oddList[i-1]
        if diff > oddMin :
            oddMin = diff
    
    evenMin = -sys.maxsize
    #evenList에서 최대값
    for i in range(1, len(evenList) ) :
        diff = evenList[i] - evenList[i-1]
        if diff > evenMin :
            evenMin = diff
    
    #odd와 even이 맨 앞끼리 맨 뒷 숫자끼리 비교
    #맨 앞 비교
    max_ = max(abs(evenList[-1] - oddList[-1]), evenList[0] - oddList[0])
    
    print(max(oddMin, evenMin, max_))

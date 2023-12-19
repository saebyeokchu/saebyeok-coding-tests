import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
weights = [int(x) for x in sys.stdin.readline().split()]

totalNumOfPossibility = int("1"* len(weights),2)
sumOfPossibility = [0] * (totalNumOfPossibility + 1)

graph = [ [0] * (len(weights) ) for i in range(0,len(weights)) ]
for _ in range(n-1):
    v, u = map(int, sys.stdin.readline().split())
    graph[v-1][u-1] = 1
    graph[u-1][v-1] = 1

def getBinStr(binNum) :
    return bin(binNum)[2:].zfill(len(weights))

def checkLinkedVillage(villageMap) :
    for i in range(0, len(villageMap)) :
        if villageMap[i] == "1" :
            for j in range(0, len(graph[i])) :
                if graph[i][j] == 1 and villageMap[j] == "1":
                    return False
    return True

for i in range(0, totalNumOfPossibility+1) :
    binStr = getBinStr(i)[::-1]
    if checkLinkedVillage(binStr) : #구성 중에 우수마을이 아니여야 하는데 우수마을인 경우 체크
        for index, char_ in enumerate(binStr) :
            if char_ == "1"  :
                sumOfPossibility[i] += weights[index]

print(max(sumOfPossibility))

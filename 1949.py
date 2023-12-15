weights = [1000,1000,3000,4000,5000,2000,2000]

nums = len(weights)+1

dp = [[0]*nums for i in range(0, nums)]
dp[1][2] = 1
dp[2][1] = 1    
dp[1][3] = 1
dp[3][1] = 1
dp[2][6] = 1
dp[6][2] = 1
dp[3][5] = 1
dp[5][3] = 1
dp[3][4] = 1
dp[4][3] = 1

#1번 마을에서 시작
route = [1]
isUsu = [0]*nums
weight = 0

while len(route) > 0 : 
    from_ = route.pop()
    #연결된 중에 우수마을이 있는지 확인
    for to_ in range(1, nums) :
        if dp[from_][to_] == 1 :
            if to_ in isUsu : 
                search(null, weight) #우수마을이 아닌걸로 설정하고 탐색
            else :
                search(null, weight + weights[to_]) #우수마을로 설정하고 탐색
                search(null, weight) #우수마을이 아닌걸로 설정하고 탐색
    
    #우수마을이 있다면 우수마을이 되면 안됨
    #우수마을이 없다면 우수마을이 될 수도 있고 안될 수도 있다

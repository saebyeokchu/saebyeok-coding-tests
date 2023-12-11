import sys

N = 4
M = ["0 10 15 20","5 0 9 10","6 13 0 12","8 8 9 0"]
K = []
dp = []

for i in range(0,4) :
    K.append(list(map(int,M[i].split())))
    dp.append([0]*(N+i))
    
print(K)
print(dp)

#1번 마을 -> 2번 마을 0011
#dp[2][0011] = dp[2][3] -> 1하고 2를 지나는 경우의 수
for i in range(0, N) :
    for j in range(0, N) :
        if K[i][j] != 0 :
            print(i,j, i+j)
            if dp[i][i+j] == 0 :
                dp[i][i+j] = K[i][j]
            else :
                dp[i][i+j] = min(min(dp[i]) + K[i][j], dp[i][i+j] )
            
print(dp)
        #K[i][j]

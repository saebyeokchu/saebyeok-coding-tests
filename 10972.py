#두개 인접한 경우를 찾는다
#뒤가 더 큰지 확인한다
#뒤에서 부터 탐색하여 인접한 앞의 값보다 큰값을 찾는다
#x2x31이고 2가 앞의 값이면 1이 아닌 3과 교환한다
#앞의 값 뒤부터 오름차순으로 정렬한다 아니 이걸 어떻게 찾아

import sys
input = sys.stdin.readline

n = int(input())
perm = list(map(int,input().split()))

for i in range(n-1, 0, -1):
    if perm[i-1] < perm[i] :
        for j in range(n-1,0,-1):
            if perm[i-1] < perm[j] :
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm = perm[:i] + sorted(perm[i:])
                print(" ".join(map(str,perm)))
                exit()
print(-1)

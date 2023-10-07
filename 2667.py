M = 7
S = ' \
0110100 \
0110101 \
1110101 \
0000111 \
0100000 \
0111110 \
0111000  '
M = []

temp = []
for s_ in S :
     if s_.isspace() and len(temp) > 0 :
         M.append(temp)
         temp=[]
     elif s_.isspace() == False :
         temp.append(int(s_))

# 0,0 부터 시작한다
# 오른쪽과 왼쪽을 탐색하고 방문을 체크한다
# 1이라면 탐색을 진행하고 0이면 탐색을 종료한다
# 모든 탐색이 종료되면 단지로 할당한다
# visited되지 않은 곳을 골라서 반복한다
# 모두 visited 될때까지
print(M)
         
         

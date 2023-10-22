N = 6 #6개 톱니바퀴
S = '\
110011 \
011100 \
110011'

L = [list(map(int,s)) for s in S.split(" ")]

A = 2 #2번의 ACTION
AD = [[1,1],[2,-1]] #1번 톱니바퀴를 시계방향으로 , 2번째 톱니바퀴를 반시게방향으로 한번씩

ad = AD[0]

start = ad[0]-1
#첫번재 톱니바퀴 선택
gear = L[start]

#첫번째 톱니바퀴를 오른쪽으로 1회회전
if ad[1] == 1 : #시계방향
    right = gear[-1:]
    left = gear[:-1]
    
    new = right + left
else :
    right = gear[1:]
    left = gear[:1]
    
    new = right + left

gear = new

#붙어있는 부분을 체크
if gear[1] == L[1][4] :
    #L[1]을 반시계방향으로 회전

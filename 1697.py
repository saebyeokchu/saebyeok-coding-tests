curr, M = map(int,input().split(' '))
#N에서 M까지 X2 , -1 , +1 해서 가장 가까이 가는방법
min_ = float("inf")

def cal(curr, oper, count) :
    global min_
    
    if oper == "x2" :
        curr = curr * 2
    elif oper == "-1" :
        curr = curr - 1
    else:
        curr = curr + 1
    
    if curr < M :
        cal(curr,"x2",count+1)
        cal(curr,"+1",count+1)
    elif curr > M :
        cal(curr,"-1",count+1)
    else :       
        min_ = min(min_,count)
        
        return
    

cal(curr,"x2",1)
cal(curr,"-1",1)
cal(curr,"+1",1)

print(min_)

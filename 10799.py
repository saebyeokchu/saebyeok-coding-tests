l = '()(((()())(())()))(())'

l = list(_ for _ in l)

stack = []
razer = 0  
piece = 0

for i in range(len(l)) :
    print(razer)
    print(stack)
    print(piece)
    print("///")
    if len(stack)==0 :
        razer = 0
    if l[i] == "(" :
        stack.append(i)
    else :
        index = stack.pop(len(stack)-1)
        
        if abs(i-index) == 1 :
            razer += 1
        else :
            piece += razer + 1

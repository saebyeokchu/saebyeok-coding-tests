l = list(_ for _ in input())

stack = []
razer = []  
piece = []

for i in range(len(l)) :
    
    if l[i] == "(" :
        stack.append(i)
    else :
        index = stack.pop(len(stack)-1)
        if abs(i-index) == 1 :
            razer.append(i-1)
        else :
            #find razer which has bigger index then pipe
            count = 0
            for r in razer :
                if r > index :
                    count += 1
            piece.append( count + 1 )
            
        if len(stack)==0 :
            razer = []
print(sum(piece))

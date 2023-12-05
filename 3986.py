n = int(input())
isGoodWord = 0

for i in range(0, n) :
    str = input()
    li = list(str)
    stack = [li[0]]

    for i in range(1, len(li)) :
        #get last value of stack
        lastIndex = len(stack)-1
        
        if  lastIndex  >= 0 and li[i] == stack[lastIndex] :
            stack.pop(lastIndex)
        else :
            stack.append(li[i])

    if len(stack) == 0 :
       isGoodWord += 1

print(isGoodWord)

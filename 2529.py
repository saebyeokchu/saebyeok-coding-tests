def sol(inputArr,find) :
    arr=[]
    
    if find == "max" :
        for i in range(9,9-len(inputArr)-1,-1):
            arr.append(i)
    else :
        for i in range(0,len(inputArr)+1):
            arr.append(i)
    
    #확장하고 범위 체크
    for i in range(0, len(arr)-1) :
        for j in range(0, len(arr)-1-i) :
            if (M[j] == "<" and arr[j] > arr[j+1]) or (M[j] == ">" and arr[j] < arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

N = int(input())
M = list(input().split(" "))

print(*sol(M,"max"),sep='')
print(*sol(M,"min"),sep='')


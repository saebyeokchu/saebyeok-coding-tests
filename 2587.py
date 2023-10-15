N = []
sum_ = 0

for n in range(5):
    val = int(input())
    sum_ += val
    N.append(val)

print(sum_ // 5)

#sort 하고 중앙값 찾기
#merge sort

#2개만 남을때까지 

def sol(arr) :
    if len(arr) < 2 :
        return arr

    mid = len(arr) // 2
    low_arr = sol(arr[:mid])
    high_arr = sol(arr[mid:])
    
    merged_arr = []
    l = h = 0
    
    while l < len(low_arr) and h < len(high_arr) :
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else :
            merged_arr.append(high_arr[h])
            h +=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr

sortedAry = sol(N)
print(sortedAry[2])


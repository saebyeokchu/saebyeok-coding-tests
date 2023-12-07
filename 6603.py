import sys

def comb(inputs,count, str_) :
    if count == 6 :
        print(str_)
        return
    
    for i in range(0, len(inputs) ) :
        item =  str(inputs[i])
        comb(inputs[i+1:], count+1, str_ + item + " ")

while True:
    list_ = list(map(int, input().split()))
    fisrt = list_[0]
    list_ = list_[1:]

    if fisrt == 0 :
        exit()

    comb(list_,0, '')
    print()
       

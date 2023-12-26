
import sys
'''
N = 5 
S = 0
l = [-7, -3, -2, 5, 8]
-7 -3 -2 5 8
'''

input_ = sys.stdin.readline()
N, S = map(int, input_.split())
input_ = sys.stdin.readline()
l = list(map(int, input_.split()))
count = 0

def find(li) :
    global count
    
    if len(li) == 0 :
        return
    
    if sum(li) == S :
        #print("answer : ",li)
        count += 1
        return
    
    for item in li:
        li.remove(item)
        find(li)
        li.append(item)
     
find( l )
print(count)

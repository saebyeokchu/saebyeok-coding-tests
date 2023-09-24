import itertools

x, y = map(int,input().split(" "))
data_list = [_ for _ in range(1,x+1)]

for i in itertools.permutations(data_list,y) :
    tuple_of_str = i
    print(' '.join(str(item) for item in tuple_of_str))

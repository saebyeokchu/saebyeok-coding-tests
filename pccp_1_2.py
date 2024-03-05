
input_list = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

shows=3
actors=5

dp = [ [0]*shows for actor in range(0, actors) ]

print(dp)

def search(parentShow, parentActor):
    for show in range(parentShow,shows) :
        for actor in range(0,actors) :
            dp[parentActor][parentShow] = max(input_list[parentActor][parentShow]+input_list[actor][show],dp[parentActor][parentShow])

for show in range(0,shows) :
        for actor in range(0,actors) :
            search(show, actor)

print(dp)

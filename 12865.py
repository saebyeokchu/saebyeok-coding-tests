mw = 50
w = [2, 5, 10, 13]
v = [10, 9, 8, 7]
d = [0] * (mw+1)

def find(ws, a) :
    if ws >= 50 :
        print(a)
        return
    
    for idx, w_ in enumerate(w) :
        if ws + w_ <= mw :
            if ( d[ws + w_] != 0 and d[ws + w_] <  a + v[idx] ) or d[ws + w_] == 0 :
                d[ws + w_] =  a + v[idx]
                find(ws + w_, a + v[idx])
            

for idx, w_ in enumerate(w) :
    find(w_, v[idx])

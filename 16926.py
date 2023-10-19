def put_chain(c, k, n , m, r, A):

def get_chain(k,n,m,A) :
    c = [0] * ((n + m - 2) * 2)
    
    i, j = k, k
    
    for _ in range(n-1):
        c[t] = A[i][j]
        i += 1; t+= 1
    for _ in range(m-1):
        c[t] = A[i][j]
        j += 1; t+= 1
    for _ in range(n-1):
        c[t] = A[i][j]
        i += 1; t+= 1
    for _ in range(m-1):
        c[t] = A[i][j]
        j -= 1; t+= 1
    
    return c

def rotate(k, n, m, r, A):
    chain = get_chain(k, n, m ,A )
    pos = len(chain) - (r % len(chain))
    rotated = chain[pos:]+chain[:pos]
    put_chain(rotated, k, n , m, r, A)

def solve(n,m,r,A) :
    for k in range(min(n,m) // 2):
        rotate(k, n, m, r, A)
    
    for i in range(n):
        print(" ".join(map(str, A[i])))

n, m, r = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(n)]

solve(n,m,r,A)

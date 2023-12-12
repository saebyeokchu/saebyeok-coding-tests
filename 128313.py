N=int(input(), 2)
M=int(input(), 2)
L = 100000

mask = 2 ** L   - 1

print(bin(N & M)[2:].zfill(L))
print(bin(N | M)[2:].zfill(L))
print(bin(N ^ M)[2:].zfill(L))
print(bin(N ^ mask)[2:].zfill(L))
print(bin(M ^ mask)[2:].zfill(L))

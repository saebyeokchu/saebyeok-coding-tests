a, b = map(int, input().split(" "))
greatestCommonDivisor = 1
leastCommonMultiple = 1

for i in range( a if a > b else b, 1, -1) :
    if a % i == 0 and b % i == 0 :
        greatestCommonDivisor = i
        break

standVal = a if a < b else b
oppositeVal = b if standVal == a else a
multiplyVal = 1
while True :
    if (standVal * multiplyVal) % oppositeVal == 0 :
        leastCommonMultiple = standVal*multiplyVal
        break
    multiplyVal += 1

print(greatestCommonDivisor)
print(leastCommonMultiple)

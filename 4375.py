while True :
    n = int(input())
    m = "1"
    while int(m) % n != 0 :
        m += "1"
    print(m)

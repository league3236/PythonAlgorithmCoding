

time = int(input())

if time % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    print(A, B, C) 
    A = TIME // 300
    B = (TIME % 300) // 60
    C = (TIME % 300) % 60 // 10
    print(A, B, C)
    
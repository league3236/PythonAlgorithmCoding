length = int(input("입력: "))

for i in range(1,length+1):
    print('O'*(length-i)+'X'*(i))
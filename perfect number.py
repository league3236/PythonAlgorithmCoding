def sub_multiple(N):
    sub_multiple = []
    for i in range(1,N):
        if(N%i==0): sub_multiple.append(i)
    # print(sub_multiple)
    if sum(sub_multiple) == N:
        # print("완전수")
        return True
    else:
        return False

N = int(input("N : "))
perfect_num = []
for i in range(2, N+1):
    if sub_multiple(i)==True:
        perfect_num.append(i)
print(perfect_num)
print(sum(perfect_num))
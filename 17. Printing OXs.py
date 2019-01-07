length = int(input("입력: "))

for i in range(1,length+1):
    print('O'*(length-i)+'X'*(i))
    
    
    
    ####################bit 이용
length = int(input("입력: "))
#
# for i in range(1,length+1):
#     print('O'*(length-i)+'X'*(i))

sum1 = 0
for i in range(6): #0-5
    sum1 = sum1 | 2**i
    print(((length - bin(sum1).count('1'))*'O')+(bin(sum1).count('1') * 'X'))
#         #000011 -> 3
#         #000111 -> 7
#         #001111 -> 15
#         #011111 -> 31
#         #111111 -> 63
# #



n = 10
pay = 4790
array1 = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
array1.reverse()

answer = 0

for i in array1:
    while pay-i>=0 :
        pay = pay-i
        answer += 1
        print(pay-i)
    
print(answer)



        
# 프로그램 실행 순서
#
# 1. 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 2. 입력받은 정수의 개수만큼 정수를 입력받는다.
# 3. 입력받은 정수의 합과 평균 값을 출력한다.
# 4. 할당된 메모리 공간을 비운다.
#
# 요구사항
#
# 1. 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 2. 사용한 공간은 마지막에 비워야 한다.
# 3. 배열을 사용하면 안된다.

# n = int(input("입력할 정수:"))
# list=[]
# sum=0
# avg=0
# for i in range(n):
#     k=int(input(str(i+1)+"번째 입력 값:"))
#     sum+=k
#

i = int(input("몇개씩 넣을거니?"))
sum1 = 0
count = i

while(count):
    count -= 1
    sum1 += int(input("정수입력"))

avg = sum1/i

print("합계 : {}, 평균 {}".format(sum1, sum1/i))
del avg, sum1

#!python
#10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이다.
# 이들의 합은 23이다. 1000미만의 자연수에서 3,5의 배수의 총합을 구하여라
list1 =[] #메모리 사용량이 급격히 증가된다. 배열이 크면 클수록 급격히 증가한다.
sum1 = 0 #최종 결과물

for i in range(10):
    if i%3==0 or i%5==0: #배수를 물으면 %를 많이 쓴다.
        list1.append(i)
print(sum(list1))


for i in range(1,1000):
    if ((i%3 == 0 )or (i%5 == 0)):
        sum1 += i
print(sum1)


#라인 하나로 끝내기
#list comprehension
print(sum(list([x for x in range(1000) if x%3==0 or x%5==0])))

#list comprehensions 배워보기
multiples = []
for n in range(1,16):
    multiples.append(n*5)
print(sum(multiples))
#위에 코드를 list comprehensions로 변경
print(sum(list([n*5 for n in range(16)])))


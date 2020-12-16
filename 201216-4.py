
# techiedelight.com/sort-binary-array-linear-time/


A = [0, 1, 0, 0, 1, 0] 
A.sort()
print(A)

m = "파이 선 잘하기 연습하기"
m = m.split()
print(m)

m.sort(key=len)
print(m)

A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

zeros = A.count(0)
print(zeros)

i = 0

while zeros:
    A[i] = 0
    zeros = zeros - 1
    i = i + 1

for i in range(i, len(A)):
    A[i] = 1


print(A)
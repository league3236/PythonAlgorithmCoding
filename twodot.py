
# 두 점의 거리 구하기
import math

def solve(first, second):
    answer = 0
    a = (first[0]-second[0])
    b = (first[1]-second[1])
    a = a*a
    b = b*b
    answer = math.sqrt(a+b)
    return answer


print(solve([3,4], [1,2]))
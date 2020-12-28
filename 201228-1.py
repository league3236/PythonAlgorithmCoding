
import math

def solution(num, array):
    array.sort()
    print(array)
    sum = 0
    for i in range(0, num):
        for j in range(0, i+1):
            sum = sum +array[j]
    print(sum)
    

print(solution(5, [3,1,4,3,2]))
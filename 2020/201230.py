# https://www.acmicpc.net/problem/5585


def solution(a):
    array = [500, 100, 50, 10, 5, 1]
    aa = 1000 - a
    answer = 0
    for i in array:
        while (aa-i >= 0):
            aa = aa-i
            answer += 1
            if aa == 0:
                return answer
    return -1


print(solution(380))
import math

def solution(progresses, speeds):
    answer = []
    li = []
    for i in range(len(progresses)):
        print(progresses[i], speeds[i])
        va = (100-progresses[i])/speeds[i]
        va = math.ceil(va)
        li.append(va)
    count = 1
    min = li[0]
    for i in range(1,len(li)):
        if min >= li[i]:
            count += 1
        elif min<li[i]:
            answer.append(count)
            count = 1
            min = li[i]
    answer.append(count)
        
    print(answer)
    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

def solution(scoville, K):
    answer = 0
    while [idx for idx in scoville if idx < K]:
        answer = answer + 1
        scoville[0] = scoville.pop(0) + scoville.pop(1)
    return answer

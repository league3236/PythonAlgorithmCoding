# 수평 직선에 탑 N대를 세웟음
# 모든 탑의 꼭대기에는 신호를 송/수긴 가능
# 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신
# 한번 수신된 신호는 다른탑으로 송신되지 않음


def solution(heights):
    answer = [0 for _ in range(len(heights))]
    for idx, value in enumerate(heights):
        height = heights[:idx]
        if len(height) == 0:
            continue
        for i in range(len(height),0,-1):
            if heights[i] > value:
                answer[idx] = i+1
                break
    return answer


print(solution([6,9,5,7,4])) # 9,9,7 # 0,0,2,2,4

def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break 
    return answer


prices = solution([1, 2, 3, 2, 3])
print(prices)
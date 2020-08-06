
# 초단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성해라

def solution(prices):
    answer = []
    for idx in range(len(prices)):
        leng = 0
        flag = 0
        for jdx in range(idx+1, len(prices)):
            leng = leng + 1
            print(idx,prices[idx], jdx, prices[jdx:])
            if prices[idx] > prices[jdx]:
                answer.append(leng)
                flag = 1
                break
        if flag == 0:
            answer.append(leng)
    return answer


prices = solution([1, 2, 3, 2, 3])
print(prices)
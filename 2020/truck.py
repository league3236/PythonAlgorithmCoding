# 다리를 지나는 트럭
# 일차선 다리를 정해진 순으로 건넘
# 모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지 
# 트럭은 1초에 1만큼 움직임
# 다리 길이는 bridge_length
# 다리 무게는 weight까지 견딤

# 길이가 2이고 10kg 무게를 견디는 다리가 있다.
# 무게가 [7,4,5,6] 인 트럭이 순서대로 시간안에 다리를 건너려면


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    
    while truck_weights:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer+bridge_length

answer = solution(2,10,[7,4,5,6])
print(answer)
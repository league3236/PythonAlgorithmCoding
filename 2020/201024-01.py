# 코스빌 주소 =
# 가장 맵지 않은 음식의 코스빌 지수 +
# (두 번째로 맵지 않은 음식의 스코빌 지수 *2 )
# Leo 가 가진 음식의 스코빌 지수를 담은 배열 scoville와 원하는
# 스코빌 지수 K가 주어질때, 모든 음식의 스코빌 지수를 K이상으로 만들기
# 위해 섞어야 하는 최소 회수를 return하도록 하는 솔루션 함수를 작성해라

# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은값은
# 언제나 인덱스 0, 즉, 이진 트리의 루트에 위치합니다. 내부적으로 min heap내의 모든 원소(k)는 항상
# 자식 원소들 (2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제된다.

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1
    return answer

print(solution([1,2,3,9,10,12], 7))

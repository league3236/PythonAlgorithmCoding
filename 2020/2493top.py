
def solution(heights):
    answer = [0]
    for height in range(1, len(heights)):
        for height1 in range(height-1,-1,-1):
            if heights[height] < heights[height1]:
                answer.append(height1+1)
                break
            elif height1 == 0 and (heights[height] >= heights[height1]):
                answer.append(0)
    return answer
        
print(solution([6,9,5,7,4]))

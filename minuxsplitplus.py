

def solution(li1):
    return [li for li in li1 if li < 0] + [li for li in li1 if li > 0]

result = solution([1,2,3,-1,-2,-3])
print(result)
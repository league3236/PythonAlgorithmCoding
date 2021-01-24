def solution(nums):
    answer = 1
    list = []
    
    get_max = int(len(nums)/2)
    nums.sort()
    
    static_num = nums[0]
    
    for i in range(len(nums)):
        if nums[i] > static_num:
            static_num = nums[i]
            answer=answer+1
    
    if get_max < answer:
        return get_max
    return answer


print(solution([3,3,3,2,2,2]))

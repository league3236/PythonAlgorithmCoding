def GymSuit_max(n, lost, reserve):
    max = n-len(lost)
    for i in lost:
        if reserve.count(i) > 0:
            reserve.remove(i)
            max+=1
        elif reserve.count(i-1) > 0:
            reserve.remove(i-1)
            max+=1
        elif reserve.count(i+1) > 0:
            reserve.remove(i+1)
            max+=1
    return max
    
GymSuit_max(5,[2,4],[1,3,5])

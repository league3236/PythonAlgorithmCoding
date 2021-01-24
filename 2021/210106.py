# https://medium.com/@edhz/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-python-2018-kakao-blind-recruitment-%EB%B9%84%EB%B0%80%EC%A7%80%EB%8F%84-%ED%92%80%EC%9D%B4-47d49cc0f19f


def solution(n , arr1, arr2):
    answer = []
    array1 = makeArray(arr1, n)
    array2 = makeArray(arr2, n)

    for i in range(n):
        temp = ''
        for j in range(n):
            if int(array1[i][j]) or int(array2[i][j]) == 1:
                temp+= '#'
            else:
                temp+= ' '
        answer.append(temp)    
    return answer

def makeArray(arr, n):
    size = n
    ret = []
    for i in range(size):
        temp = bin(arr[i])[2:]
        if len(temp) < size:
            temp = '0'*(size-len(temp)) + temp
        ret.append(list(temp))

    return ret


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(5, arr1, arr2))

# https://ychae-leah.tistory.com/197

## zip 함수
Number = [1,2,3,4,5]
Name = ['hong','gil','dong','nim','ida']

Number_name = list(zip(Number, Name))
print(Number_name)

## 반올림, 내림, 올림

# 올림
import math 
print(math.ceil(-3.14))
print(math.ceil(3.14))

# 내림
print(math.floor(-3.14))
print(math.floor(3.14))

# 반올림
print(round(3.1324))
print(round(3.1324,2))


def solution(progresses, speeds):
    answer = []
    m = 0
    history = 0
    array = list(zip(progresses, speeds))
    for key, value in array:
        done = math.ceil((100-key) // value)
        if m == 0:
            m = done
            history = 1
        elif m < done :
            answer.append(history)
            m = done
            history = 1
        elif m >= done :
            history += 1
        
    answer.append(history)

    return answer


progresses = [93, 30, 55]	
speeds = [1,30,5]

print(solution(progresses, speeds))
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
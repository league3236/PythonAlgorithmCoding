
# 숫자 하나로만 이루어지지 않은 4자리 수를 정한다. (예: 1000은 인정하되, 1111은 인정하지 않는다.)
# 첫 자리에 0이 와도 무방하다.
# 이 숫자를 크기 순으로 배열하여 두 수를 만든다. 하나는 큰 순, 하나는 작은 순으로 배열한다.
# 큰 쪽에서 작은 쪽을 빼 준다. 이때 나온 0은 유지한다.
# 이 과정을 반복하면 7번 이내로 6174가 나온다.
# 어떤 수를 입력 받고 몇번이내로 6174가 완성 되었는지 출력하는 함수를 입력하시오
#
# 단, 입력값은 정수여야 한다.
#
# 입력
#
# print(kaprekar_constant(4371))
# print(kaprekar_constant(21))
# print(kaprekar_constant(1))
# print(kaprekar_constant(1111))
# 출력
#
# 7
# 3
# False
# False

def kaprekar_constant(num):
    numlist = list(str(num))
    numlist.sort()
    orum = numlist
    print(orum)
    numlist.reverse()
    narim = numlist

    print(orum)

    print(narim)
    nownum = max(int(''.join(orum)),int(''.join(narim)))
    nownum1 = min(int(''.join(orum)),int(''.join(narim)))
    print(nownum)
    print(nownum1)

    return True

kaprekar_constant(4371)
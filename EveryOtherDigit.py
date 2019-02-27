# 모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.)
# 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.


def ciwan(num):
    num = str(num)
    num = list(num)
    for i in range(len(num)):
        if int(i)%2 == 1:
            num[i] = '*'

    return ''.join(num)

print(ciwan(123456789))

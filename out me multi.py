# 배열 [a, b, c, d]를 입력하면
# 배열[bcd, acd, abd, abc]를 출력하는 코드를 작성하시오.
# (단, 나눗셈 사용 금지)
# 입출력되는 배열은 어떤 형식이든 상관없습니다.
# 입력 예시
# 2, 6, 4, 7
# 출력 예시
# 168, 56, 84, 48

def array_out(a, b, c, d):
    list = []
    list.append(b*c*d)
    list.append(a*c*d)
    list.append(a*b*d)
    list.append(a*b*c)

    return list

print(array_out(2,6,4,7))







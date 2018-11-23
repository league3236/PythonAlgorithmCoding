# A씨는 게시판 프로그램을 작성하고 있다.
# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지 수를 리턴하는 프로그램이 필요하다고 한다.

#입력 : 총건수(M) 한페이지에 보여줄 게시물 수
#m=0 n=1 출력 0

m = int(input("m의 값을 입력하세요 : "))
n = int(input("n의 값을 입력하세요 : "))


# m n 출력
# 0 1 0
# 1 1 1
# 2 1 2
# 1 10 1
# 10 10 1
# 11 10 2
def returnPage(m,n):
    if m == 0:
        return 0
    elif m<=n:
        return 1
    elif (m%n) == 0:
        return m//n
    else:
        return m//n+1

print(returnPage(m,n))
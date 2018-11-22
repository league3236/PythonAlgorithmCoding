#A씨는 개발된 소스코드를 특정 업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것,
#공백으로 들여쓰기가된 것들이 섞여있다고 한다. 탭을 공백 4개로 만들어주는 소스코드를 만들어라

# 따옴표 세개는 전체 라인을 문자열로 바꾸는 것

# data = """
# list1 =[] #메모리 사용량이 급격히 증가된다. 배열이 크면 클수록 급격히 증가한다.
# sum1 = 0 #최종 결과물
#
# for i in range(10):
# \tif i%3==0 or i%5==0: #배수를 물으면 %를 많이 쓴다.
# \t\tlist1.append(i)
# print(sum(list1))
#
#
# for i in range(1,1000):
# \tif ((i%3 == 0 )or (i%5 == 0)):
# \t\tsum1 += i
# print(sum1)
# print(sum(list([x for x in range(1000) if x%3==0 or x%5==0])))
#
# multiples = []
# for n in range(1,16):
# \tmultiples.append(n*5)
# print(sum(multiples))
# print(sum(list([n*5 for n in range(16)])))
# """

def fileTap2Space(fname):
    with open(fname, "r", encoding="UTF8") as f:
        data = f.read()
    # return data.replace("\t"," "+4)
    print(data.replace("\t"," "+4))
filename = "1. Multiples of 3 and 5.py"
# print(fileTap2Space(filename))
fileTap2Space(filename)

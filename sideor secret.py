# 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
# 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는(여기서는 예를 들 때 3으로 지정하였다)
# 알파벳이 출력되는 것이다. 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
#
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라


def secret(_str, _int):
    _str = list(_str)
    for i in range(len(_str)):
        _str[i] = ord(_str[i])+5
        _str[i] = chr(_str[i])

    _str = ''.join(_str)
    print(_str)

secret('CAT', 5)

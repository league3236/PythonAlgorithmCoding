# 공백을 제외한
# 글자수만을 세는 코드 테스트


def string_num(_str):
    _str = list(_str)
    num = len(_str)
    for i in range(len(_str)):
        if _str[i] == ' ':
            num-=1
    return num

print(string_num("공백을 제외한 글자수만을 세는 코드 테스트"))
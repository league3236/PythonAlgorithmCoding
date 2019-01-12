# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
# 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자.


def DashInsert(str_list) :
    str_final = ''

    for x in range(str_list.__len__()):
        c = int(str_list[x])
        str_final += str(c)

        if x+1 < str_list.__len__():
            if c%2 == 0 and int(str_list[x+1])%2 == 0:
                str_final += str('*')
            elif  c%2 == 1 and int(str_list[x+1])%2 == 1:
                str_final += str('-')

    return str_final

print(DashInsert('4546793'))

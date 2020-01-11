'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

strings = input().upper()
words_list = list(set(strings))
words_num = list()
for i in words_list:
    count = strings.count(i)
    words_num.append(count)
if words_num.count(max(words_num)) >= 2:
    print('?')
else:
    print(words_list[words_num.index(max(words_num))])
# strings = input()
# strings = strings.upper()
# counter = collections.Counter(strings)
# max = 0
# flag = False
# for i in strings:
#     if max < counter[i]:
#         max = counter[i]
#         s = i
# for i in strings:
#     if i != s and counter[i] == max:
#         flag = True
# if flag == True:
#     print('?')
# else:
#     print(s)


def solution(s):
    answer = ''
    for idx, value in enumerate(s):
        print(value.isupper())
        if value.isupper() or value.isdigit():
            answer=answer+'_'
            print('hi')
        if value.isupper():
            value = value.lower()
        answer = answer+value
    return answer

result = solution('codingDojang')
print(result)

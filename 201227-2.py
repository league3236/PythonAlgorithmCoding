

def solution(s):
    answer = ""
    length = []
    mid = len(s)//2

    if len(s) == 1:
        return 1

    for i in range(1, mid+1):
        count = 1
        tempStr = s[:i]
        for j in range(0, len(s), i):
            print(s[j:j+i])
            if s[j:j+i] == tempStr:
                count += 1
            else:
                if count = 1:
                    count = ""
                answer += str(count) + tempStr
                tempStr = s[j:j+i]
                count = 1
        if count == 1:
            count = ""
        answer += str(count) + tempStr
        length.append(len(answer))
    return min(length)

print(solution("ababcdcdababcdcd"))
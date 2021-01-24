def solution(n, words):
    answer = []
    
    confer = []
    for i in range(len(words)):
        for j in range(i):
            if words[i] in words[j]:
                answer.append(int((i+1)/3))
                if (i+1)%n == 0:
                    answer.append(n)
                else:
                    answer.append((i+1)%n)
    return answer

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))

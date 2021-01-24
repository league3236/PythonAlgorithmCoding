

def solution(clothes):
    closet = {}
    answer = 1
    for name, category in clothes:
        if category in closet:
            closet[category].append(name)
        else:
            closet[category] = [name]
        print(closet)
    for key in closet.keys():
        answer = answer*(len(closet[key])+1)

    return answer-1

clothes = [["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]
print(solution(clothes))
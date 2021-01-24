'''
양의 정수 배열과 정수 s가 주어졌을 때, 합이 s가 되는 원소들의 조합이 있는지 찾으시오.

Input: A = {7, 3, 2, 5, 8}, s = 14

Output: Yes(7, 2, 5)
'''


from itertools import permutations


A = [7, 3, 2, 5, 8]
s = 14

flag = False

for i in range(1, len(A)+1):
    per = permutations(A, i)
    perList = list(per)
    for j in range(len(perList)):
        if s == sum(perList[j]):
            flag = True
            sucList = perList[j]
            break
    if flag == True:
        break

print(str(flag) + ":" + str(sucList))


# for i in range(1, len(A)+1):
#     per = permutations(A, i)
#     print(list(per))
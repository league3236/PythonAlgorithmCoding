# n개의 정수를 가진 배열이 있다.
# 이 배열은 양의정수와 음의 정수를 모두 가지고 있다.
# 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
#
# 정렬이 되고 난 후,
# 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다.
# 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.

list = [-1, 1, 3, -2, 2]
list1 = []

for i in range(list.__len__()):
    if list[i] < 0:
        list1.append(list[i])
for i in range(list.__len__()):
    if list[i] >= 0:
        list1.append(list[i])

print(list1)

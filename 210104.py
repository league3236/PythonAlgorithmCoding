
# n = 0
# array = ["happy", "new", "year"]

n = 0
array = ["aba", "abab", "abcabc", "a"]


for i in range(0, len(array)):
    list = []
    n += 1
    if len(array) == 0:
        n = 0
    for j in range(0, len(array[i])):
        if j == 0:
            list.append(array[i][j])
        elif array[i][j-1] == array[i][j]:
            continue
        elif array[i][j] in list:
            n -= 1
        else:
            continue
print(n)
        
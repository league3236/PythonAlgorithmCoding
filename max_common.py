
def max_common(a_num, b_num):
    min_num = min(a_num, b_num)
    list = []
    for i in range (1, min_num+1):
        if (a_num%i == 0 and b_num%i == 0):
            list.append(i)
    # print(max(list))
    print(list)

max_common(640,400)

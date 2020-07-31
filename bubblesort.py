

def bubbleSort(list1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j] < list1[i]:
                tmp = list1[j]
                list1[j] = list1[i]
                list1[i] = tmp
    return list1
list2 = bubbleSort([5,4,3,2,1])
print(list2)
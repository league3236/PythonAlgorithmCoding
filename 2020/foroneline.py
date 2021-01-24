
list1 = [1,2,3,4,5]

list2 = [i*2 for i in list1]
print(list2)

temp = list([2,3,4,5])
print(temp)

# 이중 for문 한줄로 작성

list3 = [i*j for j in list1 for i in list1]
print(list3)

list4 = [i for i in list1 if i>3]
print(list4)
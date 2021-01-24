
def solution(answers):
    answer = []
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    a, b, c = 0, 0, 0 
    for i in range(len(answers)):
        if (answers[i]==list1[i%len(list1)]):
            a=a+1
        if (answers[i]==list2[i%len(list2)]):
            b=b+1
        if (answers[i]==list3[i%len(list3)]):
            c=c+1
    maxs = max(a,b,c)
    if(maxs==a):
        answer.append(1)
    if(maxs==b):
        answer.append(2)
    if(maxs==c):
        answer.append(3)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
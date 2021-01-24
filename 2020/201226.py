

def binary_search(sorted_list, searchnum):
    start = 0
    end = len(sorted_list)-1

    while(start <= end):
        middle = start+(end-start)//2
        if searchnum == sorted_list[middle]:
            return middle
        elif searchnum > sorted_list[middle]:
            start = middle+1
        else:
            end = middle-1
    return -1

alist = [1,2,3,4,5,6,7,8]
print(binary_search(alist, 4))
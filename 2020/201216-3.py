
# https://www.techiedelight.com/find-sub-array-with-0-sum/


def printAllSubLists(A):

    for i in range(len(A)):
        sum = 0
        for j in range(i,len(A)):
            sum += A[j]
            if sum == 0:
                print("Sublist", (i, j))



if __name__ == '__main__':
    
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSubLists(A)
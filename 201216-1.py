# https://www.techiedelight.com/find-pair-with-given-sum-array/



def findPair(A, sum):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i]+A[j] == sum:
                print('Pair foud at index', i, "and", j)
                return

    print("Pair not found")


if __name__ == '__main__':

    A = [8, 7, 2, 5, 3, 1]
    sum = 10

    findPair(A, sum)
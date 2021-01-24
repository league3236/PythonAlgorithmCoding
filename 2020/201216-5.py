# https://www.techiedelight.com/find-duplicate-element-limited-range-array/


def findDuplicate(A):
    visited = [False] * (len(A)-1)
    # print(visited)
    for i in A:
        if visited[i-1]:
            return i 
        visited[i-1] = True

if __name__ == '__main__':
    A = [1, 2, 3, 4, 4]

    print("Duplicate element is", findDuplicate(A))



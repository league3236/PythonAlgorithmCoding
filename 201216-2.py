

def zeroSumSublist(A):
    s = set()

    s.add(0)
    sum =0

    for i in A:
        sum += i
        if sum in s:
            return True
        s.add(sum)

    return False

if __name__ == '__main__':
    A = [4, -6, 3, -1, 4, 2, 7]

    if zeroSumSublist(A):
        print("Sublist exists")
    else:
        print("Sublist do not exist")
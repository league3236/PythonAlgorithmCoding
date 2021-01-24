import sys

testcase = int(sys.stdin.readline())
for i in range(testcase):
    arr = sys.stdin.readline().split()
    print( int(arr[0])+int(arr[1]) )


a, m, d, n = map(int, input().split())

j = a

for i in range(2, n+1):
    j = j*m+d
print(j)


n = int(input())

x = list(map(int,(input().split())))
a = [0 for i in range(24)]

for j in range(n):
    a[x[j]]+=1
for k in range(1,24):
    print(a[k], end= ' ' )
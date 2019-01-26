

max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        ij = i * j
        _ij = list(str(ij))
        _ij.reverse()
        if list(str(ij)) == _ij:
            max = ij

print(max)


hash_table = list([0 for i in range(8)])
print(hash_table)
print([0 for i in range(8)])

hash_table1 = [0 for i in range(8)]
print(hash_table1)

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    return num

print(factorial(3))

def multiple(num):
    if num > 1:
        return num+multiple(num-1)
    return num

print(multiple(10))

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0]+sum_list(data[1:])


string = 'abc'
string1 = ''
for a in string:
    string1 = a+string1
print(string1)

def palindrome(data):
    if len(data) <= 1:
        return True
    if data[0] == data[-1]:
        return palindrome(data[1:-1])
    return False


print(palindrome('stsre'))
print(palindrome('aba'))


def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data-1) + func(data-2) + func(data-3)

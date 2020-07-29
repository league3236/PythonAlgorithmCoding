

numbers = [40, 35, 27, 50, 75]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot]
        more = [number for number in array[1:] if number > pivot]
        return quickSort(less)+[pivot]+quickSort(more)
result = quickSort(numbers)
print(result)
array = list(map(int, input().split()))
step = 2
for elem in range(1, len(array)):
    if elem % 2 != 0:
        if elem - step == -1:
            step = -2
        array[elem], array[elem - step] = array[elem - step], array[elem]

print(array)

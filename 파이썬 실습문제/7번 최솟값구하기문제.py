numbers = [0, 20, 100]
minValue = numbers[0]
for i in range(1,len(numbers)):
    if minValue > numbers[i]:
        minValue = numbers[i]
print(minValue)

numbers = [ [0, 20, 100], [0, 20, 100, 50, -60, 50, 100], [0, 1, 0], [-10, -100, -30] ]

for i in numbers:
    result = i[0]

    for j in i:
        if j < result:
            result = j
    print(result)
numbers = [0, 20, 100]
# 변수의 자리를 먼저 생각한다.
maxValue = numbers[0]
# range를 통해 범위를 정한다.
for i in range(1,len(numbers)):
    # 변수 자리에 있는 숫자 보다 크면 출력한다.
    if maxValue < numbers[i]:
        maxValue = numbers[i]
print(maxValue)

numbers = [ [0, 20, 100], [0, 20, 100, 50, -60, 50, 100], [0, 1, 0], [-10, -100, -30] ]

for i in numbers:
    result = i[0]

    for j in i:
        if j > result:
            result = j
    print(result)
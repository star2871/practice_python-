numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0

for i in numbers:
    if i//5 == 0:
        cnt += 1
print(cnt)
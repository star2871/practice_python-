n = int(input())
cnt = 0
for a in range(1,11):
    cnt += a
print(cnt)

n = 0
result = 1
while result < 11:
    n += result
    result += 1
    print(n)
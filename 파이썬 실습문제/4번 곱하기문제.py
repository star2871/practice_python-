# for 문
n = int(input())
cnt = 1
for a in range(1,n+1):
    cnt *= a
    print(cnt)

# while 문
n = int(input())
result = 1
a = 1
while a<= n:
    result *= a
    a += 1
print(result)
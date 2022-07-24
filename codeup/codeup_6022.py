# 첫번째 방법
s = input()
print(s[0:2])
print(s[2:4])
print(s[4:6])
# 두번째 방법
yymmdd = str(input())
result = []
cnt = 0
for _ in range(3):
    # .append 는 세로인 문자열을 가로로 나열 할수있다.
    result.append(yymmdd[cnt:cnt+2])
    cnt += 2

print(" ".join(result))
from re import I
import sys
sys.stdin = open("7_분해합.txt")

n = int(input())
result = 0

for tc in range(1, n+1):
    # 숫자를 각자수리수를 리스트에 넣기
    a = list(map(int,str(tc)))
    s = tc +sum(a)
    if s == n:
        result = tc
        break

print(result)

# 첫번째 방법
a, b = input().split()
c = int(a) + int(b)
print(c)
# 두번째 방법
import sys
a, b = map(int, sys.stdin.readline().split())
print(a + b)
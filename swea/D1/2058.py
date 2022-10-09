import sys

sys.stdin = open("2058.txt")


n = int(input())
# 각자리수의를 합하는법
a = sum(map(int, str(n)))
print(a)

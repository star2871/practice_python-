import sys

sys.stdin = open("1001.txt")
n, m = list(map(int, input().split()))
print(n-m)
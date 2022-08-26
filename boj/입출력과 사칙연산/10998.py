import sys

sys.stdin = open("10998.txt")
n, m = list(map(int,input().split()))
print(n*m)
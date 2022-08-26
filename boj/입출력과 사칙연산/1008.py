import sys

sys.stdin = open("1008.txt")
n, m = list(map(int,input().split()))
print(n/m)
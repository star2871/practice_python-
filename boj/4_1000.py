import sys

sys.stdin = open("4_1000.txt")

a, b = map(int, input().split())
print(a+b)
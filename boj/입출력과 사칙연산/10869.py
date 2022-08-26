import sys

sys.stdin = open("10869.txt")

A, B = list(map(int, input().split()))
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

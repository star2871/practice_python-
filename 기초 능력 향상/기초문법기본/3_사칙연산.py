import sys
sys.stdin = open("3_사칙연산.txt")

a, b = list(map(int,input().split()))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

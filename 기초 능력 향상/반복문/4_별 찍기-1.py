import sys
sys.stdin = open("4_별 찍기-1.txt")

n = int(input())

for tc in range(1, n+1):
    print(tc*'*')


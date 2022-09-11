import sys
sys.stdin = open("6_더블더블.txt")

n = int(input())

for tc in range(0, n+1):
    print(f'{2**tc}', end=' ')
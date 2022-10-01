import sys

sys.stdin = open("boj_10250.txt")


n = int(input())

for tc in range(n):
    H, W, N = map(int, input().split())
    a = N % H  # 층수
    b = N // H + 1  # 호수

    if N % H == 0:
        a = H
        b = N // H

    print(a * 100 + b)

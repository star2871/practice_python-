import sys
sys.stdin = open("8_홀수만 더하기.txt")

T = int(input())

for tc in range(1, T+1):
    n = list(map(int,input().split()))
    cnt = 0
    for i in range(len(n)):
        if n[i]%2==1:
            cnt+= n[i]
    print(f'#{tc} {cnt}')


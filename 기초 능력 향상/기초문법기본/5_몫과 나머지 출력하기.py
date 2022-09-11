import sys
sys.stdin = open("5_몫과 나머지 출력하기.txt")

T = int(input())

for tc in range(1, T+1):
    a, b = list(map(int,input().split()))
    print(f'#{tc} {a//b} {a%b}')
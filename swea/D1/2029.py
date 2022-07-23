import sys
sys.stdin = open("2029.txt", "r")

T = int(input())
for i in range(1,T+1):
    # int 함수를 전체에 적용 시켜준다.
    a, b = map(int, input().split())
    # 
    c, d = a//b , a%b
    print(f'#{i} {c} {d}')
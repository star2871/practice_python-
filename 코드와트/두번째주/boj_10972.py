import sys
sys.stdin = open("boj_10972.txt")

N = int(input())

M = list(map(int,input().split()))

find = False
for i in range(N-1, 0, -1):
    if M[i-1] < M[i]:  # 뒷 값이 앞 값보다 크다면
        for j in range(N-1, 0, -1):
            if M[i-1] < M[j]:
                M[i-1], M[j] = M[j], M[i-1]  # 간단한 스왑
                M = M[:i] + sorted(M[i:])
                find = True
                break
    if find:
        print(*M)  # 리스트 앞에 *를 붙이면 안에 있는 숫자들을 1 2 3 4 이런 식으로 출력할 수 있음
        break
if not find:
    print(-1)

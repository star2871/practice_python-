import sys
sys.stdin = open("1_블랙잭.txt")

n, m =list(map(int, input().split()))

card =list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i]+ card[j]+ card[k] > m:
                continue
            else:
                # result 변수에는 M의 값 또는 M에 가장 가까운 값이 저장될것이다.
                result = max(result, card[i]+card[j]+card[k])

print(result)
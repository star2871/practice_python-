import sys

sys.stdin = open("1_슈퍼마리오.txt")

list_n = []
cnt = 0
for tc in range(10):
    n = int(input())
    list_n.append(n)

for i in list_n:
    cnt += i
    if cnt >= 100:
        # 여기서 100 가까운수가 두개가 나오기 때문에 둘을 비교해야한다.
        if cnt - 100 > 100 - (cnt - i):
            cnt -= i
            break
print(cnt)

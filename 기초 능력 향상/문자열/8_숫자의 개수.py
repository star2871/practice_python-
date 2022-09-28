import sys

sys.stdin = open("8_숫자의 개수.txt")

a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
list_a = [0] * 10

for tc in d:
    # 여기 부터 생각이 안낫다. 해보니까 위에서 10개를 정의 했으니까
    # 그 한칸마다 0~9까지 있다고 생각하고 집어넣으면 된다.
    list_a[int(tc)] += 1
# 이거는 list를 밑으로 print하기 위해서 쓴것이다.
for i in list_a:
    print(i)

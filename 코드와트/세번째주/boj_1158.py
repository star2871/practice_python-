import sys

sys.stdin = open("boj_1158.txt")

N, K = list(map(int, input().split()))

queue = []
result = []
for i in range(1, N + 1):
    # queue에 1~8까지 순서대로 넣는다.
    queue.append(i)

i = 0
while queue:
    # i는 3이다.
    i = (i + (K - 1)) % len(queue)
    # 여기서 i는 index값이다.
    # queue = [1,2,3,4,5,6,7]
    # queue = [2,3,4,5,6,7,1]
    # queue = [3,4,5,6,7,1,2]
    # queue = [4,5,6,7,1,2] result=[3]
    result.append(queue.pop(i))

print("<" + ", ".join(map(str, result)) + ">")

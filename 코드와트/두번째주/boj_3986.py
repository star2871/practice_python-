import sys
sys.stdin = open("boj_3986.txt")

N = int(input())
res = []

# 단어의 수만큼 반복하면 단어를 확인
for _ in range(N):
    s = list(map(str, sys.stdin.readline().strip()))

    stack = [0]
    # 반복문으로 문자열을 확인
    for i in s:
        # 스택의 마지막 요소와 현재 탐색하고 있는 요소와 같으면
        # 팝해준다.
        if stack[-1] == i:
            stack.pop()
        # 그렇지 않다면 스택에 추가한다.
        else:
            stack.append(i)

    # 스택에 길이가 1이면 아치형으로 모두 연결된 것으로 좋은 단어이다.
    # 처음에 스택에 0을 넣었기 때문에 길이가 1
    if len(stack) == 1:
        res.append(1)

print(len(res))



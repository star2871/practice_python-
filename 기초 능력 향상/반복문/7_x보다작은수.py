import sys
sys.stdin = open("7_x보다작은수.txt")

n, a = list(map(int,input().split()))

c = list(map(int,input().split()))


for i in range(len(c)):
    if c[i] < a:
        print(c[i], end=' ')
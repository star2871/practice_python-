import sys
sys.stdin = open("9_간단한 N 의 약수.txt")

n = int(input())

for tc in range(n):
    if n%(tc+1)==0:
        print(tc+1, end=" ")
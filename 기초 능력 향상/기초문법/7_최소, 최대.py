import sys
sys.stdin = open("7_최소, 최대.txt")

T = int(input())


n = list(map(int,input().split()))
print(min(n), max(n))
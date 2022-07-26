import sys

sys.stdin = open("18_기찍 N.txt")

N = int(input())

for i in range(N+1,0,-1):
    print(i)
import sys
sys.stdin = open("3_기찍 N.txt")

n = int(input())

for tc in range(n, 0, -1):
    print(tc)
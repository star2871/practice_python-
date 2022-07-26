from re import I
import sys

sys.stdin = open("16_합.txt")

n = int(input())
cnt = 0
for i in range(1,n+1):
    cnt = cnt + i
    i +=1
print(cnt)
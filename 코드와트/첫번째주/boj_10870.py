import sys
sys.stdin=open("boj_10870.txt")


n= int(input())
# 피보나치수열 하는법 s=[0, 1] 처음두수를 넣는다.
s=[0, 1]
for tc in range(2,n+1):
    s.append(s[tc-1] + s[tc-2])
print(s[n])
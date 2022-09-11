import sys
sys.stdin = open("1_합.txt")

n = int(input())
list_n=[]
for tc in range(1, n+1):
    list_n.append(tc)
print(sum(list_n))
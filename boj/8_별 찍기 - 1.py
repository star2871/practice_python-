import sys

sys.stdin = open("8_별 찍기 - 1.txt")
num = int(input())
for i in range(1,num+1):
    # if를 넣을 필요없다.
    print('*'*i)

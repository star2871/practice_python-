import sys
sys.stdin = open("10_음계.txt")

list_num =[1, 2, 3, 4, 5, 6, 7, 8]

n = list(map(int,input().split()))

if n == list_num:
    print('ascending')
elif n == list_num[::-1]:
    print('descending')
else:
    print('mixed')
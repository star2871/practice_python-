import sys

sys.stdin = open("15_구구단.txt")

n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')

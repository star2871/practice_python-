import sys
sys.stdin = open("5_구구단.txt")

n = int(input())

for tc in range(1, 10):
    print(f'{n} * {tc} = {n*tc}')

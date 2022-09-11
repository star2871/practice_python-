import sys
sys.stdin = open("1_두 수 비교하기.txt")

a, b = list(map(int,input().split()))

if a< b:
    print('<')
elif a> b:
    print('>')
else:
    print('==')
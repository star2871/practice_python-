import sys
sys.stdin = open("6_숫자의 합.txt")

n = int(input())

# 안붙어잇는 숫자는 이렇게 뽑으면 된다.
num = map(int,input())
print(sum(num))
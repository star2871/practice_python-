from re import I
import sys

sys.stdin = open("1_문자열 반복.txt")

T = int(input())

for tc in range(T):
    num, s = input().split()
    text=''
    for tc in s:
        # 이렇게 더해 나가면 알아서 sorted()를 해준다.
        text += int(num)*tc
    print(text)
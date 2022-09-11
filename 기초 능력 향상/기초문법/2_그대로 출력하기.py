import sys
sys.stdin = open("2_그래로 출력하기.txt")
# 첫번째 방법
# for tc in sys.stdin:
#     print(tc, end='')

# 두번째 방법
while True:
    try:
        print(input())
    except EOFError:
        break
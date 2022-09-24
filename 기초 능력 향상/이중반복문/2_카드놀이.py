import sys

sys.stdin = open("2_카드놀이.txt")


A = list(map(int,input().split()))
B = list(map(int,input().split()))

ant = bnt = 0
for i in range(10):
    if A[i] > B[i]:
        ant += 3
    elif A[i] < B[i]:
        bnt += 3
    else:
        ant += 1
        bnt += 1
print(ant, bnt)
if ant > bnt:
    print('A')
elif ant < bnt:
    print('B')
elif ant == bnt == 10:
    print('D')
else:
    # 여기서 역순으로해서 늦게 이기는쪽을 구할 수 있다.
    for i in range(1, 11):
        if A[-i] > B[-i]:
            print('A')
            break
        elif A[-i] < B[-i]:
            print('B')
            break
        else:
            continue


import sys
sys.stdin = open("1_차집합.txt")

a, b = map(int,input().split())

c = set(map(int,input().split()))
d = set(map(int,input().split()))

# set을 사용하면 차집합 할수있다.
ress = c-d
# set을 정렬하면 리스트로 나온다.
res =sorted(ress)
print(len(res))


if len(res) !=0:
    # *은 list에서 1칸띄운 값으로 빼낼수 있다.
    print(*(res))
import sys
sys.stdin = open("2_나머지.txt")

n_list=[]
for tc in range(1, 11):
    n = int(input())
    # 나누는걸 같이 넣을 생각을 못함
    n_list.append(n%42)
print(len(set(n_list)))

    
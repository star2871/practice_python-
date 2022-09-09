import sys
sys.stdin = open("3_개수세기.txt")
# 딕셔너리 방법
T = int(input())
N_list = list(map(int, input().split()))
k = int(input())

dictionary = {i : N_list[i] for i in range(len(N_list))}

cnt = 0
for key, value in dictionary.items():
    if value == k:
        cnt+= 1
print(cnt)

# 다른 방법
# T = int(input())
# N_list = list(map(int, input().split()))
# k = int(input())
# cnt = 0

# for i in N_list:
#     if i == k:
#         cnt += 1
        
# print(cnt)

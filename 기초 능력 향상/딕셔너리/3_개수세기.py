import sys
sys.stdin = open("3_개수세기.txt")

# dict={"a":1, "b":4, "c":1, "d":2, "e":4, "f":2, "g":4, "h":2, "i":3, "j":4, "k":4}
# T = int(input())
# N_list = list(map(int, input().split()))
# k = int(input())
# cnt = 0
# for key, value in dict.items():
#     if value == k:
#         cnt+= 1
# print(cnt)

T = int(input())
N_list = list(map(int, input().split()))
k = int(input())
cnt = 0

for i in N_list:
    if i == k:
        cnt += 1
        
print(cnt)

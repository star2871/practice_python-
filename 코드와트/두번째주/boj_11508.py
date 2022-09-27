import sys
sys.stdin = open("boj_11508.txt")

N = int(input())
milk_list=[]
cost = 0
for tc in range(N):
    milk_list.append(int(input()))
    # reverse=True 역정렬 할 수 있다.
milk_list.sort(reverse=True)
    
	# 내림차순으로 정렬을 해놨으니, 3번째로 들어오게 되는 값만 제외시키면 정답이 된다.
    # ex) cost += m[0],m[1],m[3],m[4],m[6],m[7]...
    # 훨씬 간결한거같다...
for tc in range(N):
    if(tc%3!=2):
        cost += milk_list[tc]
print(cost)
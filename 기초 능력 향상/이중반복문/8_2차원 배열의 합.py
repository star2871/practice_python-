import sys

sys.stdin = open("8_2차원 배열의 합.txt")

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * (m+1) for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = matrix[i-1][j-1] + arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
 
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1])
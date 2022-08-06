import sys

sys.stdin = open("1_2557.txt")

a = int(input())
b = int(input())
c = int(input())

d = a*b*c
list_=[0]*10
for tc in str(d):
    list_[int(tc)] += 1

for i in list_:
    print(i)
        
        

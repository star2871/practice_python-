import sys

sys.stdin = open("11_두 수 비교.txt")
num1 , num2 = input().split()
num1 = int(num1)
num2 = int(num2)
if (num1 < num2):
    print('<')
elif (num1 > num2):
    print('>')
else:
    print('==')
    
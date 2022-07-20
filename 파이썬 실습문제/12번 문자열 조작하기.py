word = 'apple'
#변수를 빈공간으로 정의한다.
result = ''
for i in word:
    if i != 'a':
        # 계속 문자를 더해 나가는것이다.
        result = result + i
print(result)
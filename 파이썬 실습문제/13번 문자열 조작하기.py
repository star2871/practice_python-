word = 'apple'
cnt = ''
for i in word:
    # 뒤에서 부터 더하는 것이다.
    cnt = i + cnt
print(cnt)
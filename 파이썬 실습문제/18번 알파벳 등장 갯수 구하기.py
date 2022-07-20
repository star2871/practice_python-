word = 'banana'
word_counter = {}
for i in word:
    # if not 을 쓰는게 중요하다.
    # 안나오면 1을 둔 상태에서 시작한다.
    if not i in word_counter:
        word_counter[i] = 1
    # 그 밖에는 계속 더해 나간다.
    else:
        word_counter[i] = word_counter[i] + 1
print(word_counter)

# 디셔너리 값을 중괄호가 없는 형태로 출력할수있다.
for key in word_counter:
    print(key, word_counter[key])


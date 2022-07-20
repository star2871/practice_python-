word = 'apple'
cnt = 0
# 등장 여부 확인한거 이기 때문에  len함수를 쓸필요없다.
for i in word:
    # 리스트를 사용하고싶으면 in을 사용해라.
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)
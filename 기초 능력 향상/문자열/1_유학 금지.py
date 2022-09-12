import sys
sys.stdin = open("1_유학 금지.txt")

word_='CAMBRIDGE'

word = input()

for i in range(len(word)):
    # 여기서 [i]를 빼먹었다. 빼먹지 말아라 주의!
    if word[i] not in word_:
        print(word[i], end='')
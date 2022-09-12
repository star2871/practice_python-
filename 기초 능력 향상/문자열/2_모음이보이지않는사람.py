import sys
sys.stdin = open("2_모음이보이지않는사람.txt")

word_='aeiou'

T= int(input())

for tc in range(1, T+1):
    word = input()
    result =''
    for i in range(len(word)):
        if word[i] in word_:
            # 모음 일때까지 계속 하다가 자음이 나오면 더하는 result에 넣는거다.
            continue
        result += word[i]
    
    print(f'#{tc} {result}')
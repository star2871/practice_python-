import sys
sys.stdin = open("2_문서 검색.txt")


textfile = input()
word = input()
cnt = 0
# 현재 인덱스 번호
index = 0

# 문자열을 하나씩 받으면서
for i in range(len(textfile)):
    # 중복되는 단어를 포함하려고 할 때 건너뛰기
    if index > i:
        continue
    # 찾는 단어와 문서의 단어가 같을때 개수 증가
    if word == textfile[i: i+len(word)]:
        cnt += 1
        # 인덱스 번호는 동시에 셀수 없는 가장 가까운 번호로 이동
        index = i + len(word)

print(cnt)


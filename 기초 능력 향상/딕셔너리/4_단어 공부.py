import sys
sys.stdin = open("4_단어 공부.txt")

string = input().upper()
dic = dict()

for i in range(len(string)):
    if string[i] in dic:
        dic[string[i]] += 1
        
    else:
        dic[string[i]] = 1

answer = []
for key, value in dic.items():
    if value == max(dic.values()):
        answer.append(key)
        
if len(answer) != 1:
    print('?')
else:
    print(answer[0])
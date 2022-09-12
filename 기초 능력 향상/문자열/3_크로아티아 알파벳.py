import sys
sys.stdin = open("3_크로아티아 알파벳.txt")

cr_word = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for i in cr_word:
    # 여기서 0으로 대체하는 이유는 어차피 크로아티아 알파벳 갯수를 세는 거기 때문에 다세면 된다.
    word = word.replace(i, "0")

print(len(word))
# 첫번째 방법
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
# 두번째 방법
word = list(str(input()))
# join 함수는 .join(['a', 'b', 'c']) = "abc" 파이썬리스트를 문자열로 합칠수있다.
print("\n".join(word))
number = [0, 20, 100, 40]
second_num = float("-inf")
max_num = float("-inf")

for n in number:
    if max_num < n:
        second_num = max_num
        max_num = n
    elif second_num < n < max_num:
        second_num = n
print(second_num)
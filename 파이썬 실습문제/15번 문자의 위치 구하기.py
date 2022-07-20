word ='banana'
# rage , len함수를 통해 범위와 마지막위치를정한다.
for i in range(len(word)):
    # [] 'a'의 위치를 찾을수있다.
    if word[i] == 'a':
        print(i)
        # for문을 다돌았다는 뜻은
        # 한번도 break에 안걸렸다.
        # 즉 , a는 없었다.
        break
else:
    print(-1)
def solution(participant, completion):
    answer = ''
    # 정렬을 해놓고 동일 index 번호끼리 비교
    participant.sort()
    completion.sort()

    for tc in range(len(completion)):
        # 양쪽 배열을 다 정렬했기 때문에, 같은 index의 값이 다르다면, Participant[index] 값이 정답이 될 것이다.
        if participant[tc] != completion[tc]:
            return participant[tc]
            # completion에서 알파벳 순서 상 제일 뒤에 있는 선수가 완주하지 못했다면 찾을 방법이 없다.
            # -1을통해 마지막 값을 반환한다.
    return participant[len(participant)-1]

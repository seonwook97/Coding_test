def solution(n, words):
    for i in range(1, len(words)):
        # 끝말잇기 규칙: 앞단어 끝 문자 = 뒷단어 첫문자, 이전에 나왔던 단어가 나오면 안됨
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            order = (i % n) + 1 # 진행 순서 번호
            cnt = (i // n) + 1 # 한 사람의 턴 횟수 -> 차례
            break

        else:
            order, cnt = 0, 0 # 탈락자가 없을 경우

    answer = [order, cnt]
    return answer



# 튜플
def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key=len)
    answer = []
    for item in s:
        num = item.split(',')
        for item2 in num:
            if int(item2) not in answer:
                answer.append(int(item2))
    return answer



# 프린터
def solution(priorities, location):
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                if i == location:
                    break
        else:
            continue
        break
    return c
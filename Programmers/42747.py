# 완전탐색
def solution(citations):
    citations.sort() # 정렬
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            answer = len(citations) - idx
            return answer
    return 0
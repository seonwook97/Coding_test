# 위장
from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for k, v in clothes:
        clothes_dict[v].append(k)

    for k in clothes_dict.keys():
        answer = answer * (len(clothes_dict[k]) + 1) # 안 입은 경우 + 1

    answer = answer - 1 # 아무것도 안 입는 경우 제외
    return answer






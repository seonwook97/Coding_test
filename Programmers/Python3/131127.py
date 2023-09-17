from collections import Counter

def solution(want, number, discount):
    date_cnt = 0
    temp_dict = dict(zip(want, number))
    # print(sum(temp_dict))
    for i in range(len(discount) - sum(number) + 1):
        if temp_dict == Counter(discount[i:i+10]):
            date_cnt += 1
        
    return date_cnt
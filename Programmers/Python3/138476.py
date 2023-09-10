def solution(k, tangerine):
    temp_dict = dict()
    cnt = 0
    for i in tangerine:
        if i in temp_dict:
            temp_dict[i] += 1
        
        else:
            temp_dict[i] = 1

    temp_dict = sorted(temp_dict.items(), key=lambda x:x[1], reverse=True)

    for item in temp_dict:
        k -= item[1]
        cnt += 1
        if k <= 0:
            break
            
    return cnt
    
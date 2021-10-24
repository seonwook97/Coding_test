def solution(s):
    dic_num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = ''

    for key in dic_num.keys():
        if key in s:
             s = s.replace(key, dic_num[key])
    return int(s)

# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))





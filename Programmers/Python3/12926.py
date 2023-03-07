# 시저 암호
def solution(s, n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    for c in s:
        if c in ' ':  # 문자 사이의 공백
            result += ' '

        elif c in lower:
            index_loc = lower.find(c) + n
            result += lower[index_loc % 26]  # 나머지를 통해 index_loc의 값이 알파벳 개수를 초과하여도 값을 반환
            
        elif c in upper:
            index_loc = upper.find(c) + n
            result += upper[index_loc % 26]

    return result

# print(solution('AB', 1)) -> BC
# print(solution('z', 1)) -> a
# print(solution('a B z', 4)) -> e F d

# 핸드폰 번호 가리기
def solution(a):
    a = '*' * len(a[:-4]) + a[-4:]
    return a

# print(solution('01033334444'))





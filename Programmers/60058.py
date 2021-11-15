# 문자열을 u와 v로 분리하는 함수
def seperate(p):
    left_count = 0
    right_count = 0
    for idx, i in enumerate(p):
        if i == '(':
            left_count += 1
        elif i == ')':
            right_count += 1
        # 더이상 나눠질 수 없는 올바른 괄호문자열 찾음
        if left_count == right_count:
            return p[:idx + 1], p[idx + 1:]  # u,v


def isBalanced(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ''

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = seperate(p)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if isBalanced(u):
        return u + solution(v)  # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer = '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다. 
        answer += ')'

        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        # 4-5. 생성된 문자열을 반환합니다.
        return answer




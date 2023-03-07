# 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == '(': # '('는 stack에 추가 -> 추후 닫는 괄호와 pop
            stack.append(i)
        else:
            if not stack: # 스택이 비었는데 역괄호로 시작하였으므로 False 반환
                return False
            else:
                stack.pop() # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거

    if not stack:
        return True

    else:
        return False




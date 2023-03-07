# 괄호 회전하기
def solution(s):
    answer = 0
    temp = list(s)

    for _ in range(len(s)):

        stack = []
        for i in range(len(temp)):
            if len(stack) > 0:
                if stack[-1] == '[' and temp[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and temp[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and temp[i] == '}':
                    stack.pop()
                else:
                    stack.append(temp[i])
            else:
                stack.append(temp[i])
        if len(stack) == 0:
            answer += 1
        temp.append(temp.pop(0))

    return answer
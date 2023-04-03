import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def infix_to_postfix(infix):
    # 우선순위 딕셔너리: *, / > +, - > (
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    postfix = []
    for char in infix:
        # 피연산자인 경우
        if char.isdigit():
            postfix.append(char)

        # 왼쪽 괄호인 경우
        elif char == '(':   
            stack.append(char)

        # 오른쪽 괄호인 경우
        elif char == ')':           
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            # 왼쪽 괄호를 스택에서 제거
            stack.pop()  

        else: # 연산자인 경우
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())

            stack.append(char)

    # 스택에 남은 모든 연산자를 출력
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

formula = input()
print(infix_to_postfix(formula))

# end = time.time()
# print(f"{end - start:.5f} sec")
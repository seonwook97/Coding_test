import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit(): 
            stack.append(int(token))

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = evaluate(token, operand1, operand2)
            stack.append(result)

    return stack.pop()

def evaluate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    
    elif operator == '-':
        return operand1 - operand2
    
    elif operator == '*':
        return operand1 * operand2
    
    elif operator == '/':
        return operand1 / operand2

formula = input()
print(evaluate_postfix(formula))

# end = time.time()
# print(f"{end - start:.5f} sec")
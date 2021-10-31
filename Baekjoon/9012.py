# 메모리: 29200KB, 시간: 72ms
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    vps = list(input().rstrip())
    stack = []
    flag = True
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])

        elif vps[i] == ')':
            if len(stack) != 0:
                stack.pop()

            else:
                flag = False  # 스택이 빈 상태에서 닫는 괄호가 왔으므로 VPS가 아님

    if len(stack) != 0 or not flag:  # 결국 스택에 괄호가 남아있거나 or 스택이 빈 상태에서 닫는 괄호가 오면 VPS가 아님
        print('NO')

    else:
        print('YES')














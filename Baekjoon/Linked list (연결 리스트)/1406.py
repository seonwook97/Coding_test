# 메모리: 39620KB, 시간: 348ms
import sys
input = sys.stdin.readline

s = list(input().rstrip())
cmd_num = int(input())
edit_s = []
for i in range(cmd_num):
    cmd = input().split()

    if cmd[0] == 'L' and s:
        edit_s.append(s.pop())

    elif cmd[0] == 'D' and edit_s:
        s.append(edit_s.pop())

    elif cmd[0] == 'B' and s:
        s.pop()

    elif cmd[0] == 'P':
        s.append(cmd[1])

print(''.join(s + edit_s[::-1]))

# s와 edit_s를 각각 다른 두개의 스택
# 커서는 s의 top
# 커서를 왼쪽으로 움직이면 s의 값을 pop하여 edit_s로 append
# 커서를 오른쪽으로 움직이면 edit_s의 값을 pop하여 s로 append











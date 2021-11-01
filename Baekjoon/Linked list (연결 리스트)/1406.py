import sys
input = sys.stdin.readline

s = [input().rstrip()]
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

print(''.join(s + list(reversed(edit_s))))










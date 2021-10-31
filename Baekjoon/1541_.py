# 메모리: 29200KB, 시간: 68ms    
# s = '55-50+40' # 55 - (50 + 40) <= 괄호안에 덧셈연산자가 포함되고 바깥 연산에 -만 남을 때 최소값
import sys
input = sys.stdin.readline
s = input().split('-')
num_list = []

for item in s:
    sum = 0
    a = item.split('+')
    for item in a:
        sum += int(item)
    num_list.append(sum)

for i in range(1, len(num_list)):
    num_list[0] -= num_list[i]

print(num_list[0])



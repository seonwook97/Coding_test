# 메모리: 29980KB, 시간: 3836ms
n = int(input())
n_list = []
i = 0
while i < n: # 왜 for문으로 하면 시간초과가 뜨는것인가..
    num = int(input())

    if num != 0:
        n_list.append(num)

    else:
        n_list.pop()

    i += 1

print(sum(n_list))

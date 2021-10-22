import sys
input = sys.stdin.readline

X = int(input())
count = 0
num_list = []

for i in range(1, X + 1):
    if i < 100:
        count += 1
    elif i == 1000:
        continue
    else:    # 3자리수일 때
        for num in str(i):
            num_list.append(int(num))

        d_1 = num_list[0] - num_list[1]; d_2 = num_list[1] - num_list[2]
        if d_1 == d_2:
            count += 1

print(count)
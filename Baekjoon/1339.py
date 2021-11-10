import sys
input = sys.stdin.readline

n = int(input())
s_list = [input().rstrip() for i in range(n)]
s_list = sorted(s_list, reverse=False)
alpha_dict = {}


for word in s_list:
    i = 1
    for s in word:
        alpha_dict.setdefault(s, list())
        alpha_dict[s].append(10 ** (len(word) - i))
        i += 1

for k, v in alpha_dict.items():
    alpha_dict[k] = sum(v)

alpha_dict = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)

num = 9
sum = 0
for i in range(len(alpha_dict)):
    sum += (num * alpha_dict[i][1])
    num -= 1

print(sum)



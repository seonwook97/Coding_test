import sys
input = sys.stdin.readline
W, N = map(int, input().split()) # W:배낭무게, N:귀금속종류개수

temp_lst = []
for _ in range(N):
    w, p = map(int, input().split())
    temp_lst.append([w, p])
temp_lst = sorted(temp_lst, key=lambda x:-x[1])
# print(temp_lst)

maxVal = 0
for item in temp_lst:
    if item[0] < W:
        W -= item[0]
        maxVal += (item[0] * item[1])
    else:
        maxVal += (W * item[1])
        break

print(maxVal)


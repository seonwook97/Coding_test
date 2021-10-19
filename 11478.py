S = input()
S_part = set()
# for i in range(0, len(S)):
#     for j in range(0, len(S) - i):
#         S_part.add(S[j :j+i+1])
for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        S_part.add(temp)

print(len(S_part))



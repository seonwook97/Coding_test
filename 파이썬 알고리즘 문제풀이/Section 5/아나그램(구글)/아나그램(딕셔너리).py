import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break

    else:
        print("NO")
        break

else:
    print("YES")

# code2
# a = input()
# b = input()
# sH = dict()
# for x in a:
#     sH[x] = sH.get(x, 0) + 1

# for x in b:
#     sH[x] = sH.get(x, 0) - 1

# for x in a:
#     if(sH.get(x) > 0):
#         print("NO")
#         break

# else:
#     print("YES")
# end = time.time()
# print(f"{end - start:.5f} sec")
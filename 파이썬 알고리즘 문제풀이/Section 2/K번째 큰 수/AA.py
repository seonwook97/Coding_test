# 반복문 활용
import sys
# sys.stdin = open('in1.txt', 'rt')
n, k = map(int, input().split())
nums = list(map(int, input().split()))
# add_nums = set() # 3장을 뽑아 모든 경우를 합함
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             add_nums.add(nums[i] + nums[j] + nums[m])

# add_nums = list(add_nums)
# add_nums.sort(reverse=True)
# print(add_nums[k-1])

# 패키지 활용 : Combination(조합)
from itertools import combinations

comb_nums = list(combinations(nums, 3))
add_nums = set()
for comb in comb_nums:
    add_nums.add(sum(comb))
add_nums = list(add_nums)
add_nums.sort(reverse=True)
print(add_nums[k-1])

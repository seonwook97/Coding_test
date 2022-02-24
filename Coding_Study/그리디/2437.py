# 1 1 2 3 6 7 30 -> 추의 조합으로 나타낼 수 없는 합의 최소라하여 일단 오름차순 정렬
# 1 1 2 3 6 7 30일 경우 측정할 수 없는 양의 정수 무게의 min = 21
# 1 2 3 6 30일 경우 측정할 수 없는 양의 정수 무게의 min = 13
# 1 2 3 30일 경우 측정할 수 없는 양의 정수 무게의 min = 7
# 1 2 30일 경우 측정할 수 없는 양의 정수 무게의 min = 4

# 결국 오름차순 정렬된 숫자들이 있을 때, (앞에서부터 누적된 합 + 1 < 다음 숫자) 일 때,
# 앞에서부터 누적된 합 + 1이 구하고자하는 측정할 수 없는 양의 정수 무게의 min값
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
# print(num_list)
num_list.sort()
min_val = 0
for num in num_list:
    if min_val + 1 < num:
        break

    else:
        min_val += num

print(min_val + 1)

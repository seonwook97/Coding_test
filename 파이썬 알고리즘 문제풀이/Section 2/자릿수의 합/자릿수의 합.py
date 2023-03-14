import sys
from collections import defaultdict
# sys.stdin = open('in1.txt', 'rt')
n = int(input())
num_list = list(map(int, input().split()))
sum_list = defaultdict(list)

def digit_sum(x):
    sum = 0 # 나머지를 통한 자릿수 합 변수 초기화
    while x > 0: # 몫이 0이 될 때까지
        sum += x % 10
        x //= 10
    return(sum)

for num in num_list:
    sum_list[digit_sum(num)].append(num)

print(sum_list[max(sum_list.keys())][0]) # 자릿수가 같을 경우 먼저 나온 숫자 출력

# 또 다른 방법 : 자릿수 합 함수 ->  타입 변환을 활용, 최대값 찾기 -> 완전탐색
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum

# max = 0
# for num in num_list:
#     sum_digit = digit_sum(num)
#     if sum_digit > max:
#         max = sum_digit
#         answer = num 




    
    




    

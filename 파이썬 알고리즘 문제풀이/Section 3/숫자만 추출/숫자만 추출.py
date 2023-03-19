import math
import time
import sys

# sys.stdin = open('in1.txt', 'rt')
word = input()

# 실행시간 체크
# start = time.time()

# code
word_digit = ''
for char in word:
    if char.isdigit():
        word_digit += char

word_digit = int(word_digit)

def count_divisors(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    
    return cnt

print(word_digit)
print(count_divisors(word_digit))

# end = time.time()
# print(f"{end - start:.5f} sec")
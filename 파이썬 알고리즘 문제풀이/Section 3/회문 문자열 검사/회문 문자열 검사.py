import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')

# 실행시간 체크
# start = time.time()

# code
n = int(input())
word_list = [input() for i in range(n)]

def check_palindrome(x):
    if x == x[::-1]:
        return 'YES'
    
    else:
        return 'NO'

for idx, word in enumerate(word_list):
    print('#{} {}'.format(idx + 1, check_palindrome(word.lower())))

# end = time.time()
# print(f"{end - start:.5f} sec")
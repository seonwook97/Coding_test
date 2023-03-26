import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
# 조건
## (1) 라이브의 순서가 그대로 유지
## (2) 한 DVD에 녹음하기 위해 처음과 끝 사이에 있는 트랙들을 모두 포함
## (3) DVD 용량(녹화 가능 길이)은 최소
## (4) M개의 DVD는 같은 크기
def count(size):
    cnt = 1
    sum = 0
    for x in track_list:
        if sum + x > size: # 가능 저장 용량 초과
            cnt += 1
            sum = x
        
        else:
            sum += x
    
    return cnt

n, m = map(int, input().split()) # n은 트랙 수, m은 DVD 개수 
track_list = list(map(int, input().split()))
max_track = max(track_list)
left = 1
right = sum(track_list)
while left <= right:
    mid = (left + right) // 2
    if mid >= max_track and count(mid) <= m: # DVD의 용량은 트랙의 최대값보단 크거나 같아야 함
        result = mid
        right = mid -1
    
    else:
        left = mid + 1

print(result)

# end = time.time()
# print(f"{end - start:.5f} sec")
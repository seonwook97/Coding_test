import sys
# sys.stdin = open('in1.txt', 'rt')
T = int(input()) # T개의 case
for i in range(T):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    # print(nums)
    nums = nums[s-1:e] # s번째부터 e까지
    nums.sort() # 오름차순 정렬 
    print('#{} {}'.format(i+1, nums[k-1])) # k번째 수 출력


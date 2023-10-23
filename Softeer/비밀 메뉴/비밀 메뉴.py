import sys
input = sys.stdin.readline

m, n, k = map(int, input().split()) # m, n: 비밀메뉴조작법을 나타내는 정수 개수, 정수는 1이상 k이하
secret_lst = list(map(int, input().split())) # 비밀메뉴조작법
user_lst = list(map(int, input().split())) # 사용자조작

# 확인
def check(m, n, secret_lst, user_lst):
    for i in range(n-m+1):
        cnt = 0
        for j in range(i, m+i):
            if secret_lst[j-i] == user_lst[j]:
                cnt += 1
                continue
            
            else:
                break
        
        if cnt == m:
            return 'secret'

    return 'normal'

print(check(m, n, secret_lst, user_lst))

    

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

# 조건에 부합하는 가능한 (i, j) 쌍을 count하는 함수
# 문제 조건이 i < j 이며 s[i] == 'A' && s[j] == 'B'를 만족해야하므로
# 가능한 (i, j) 쌍의 개수 = A를 기준으로 뒤의 B의 수의 총합
# 예를 들어 문자열 'ABBABBABB'가 있을 때 가능한 좌표 쌍의 개수는 6 + 4 + 2 = 14개
def check(sentence):
    cnt = 0
    for i in range(n-1):
        if sentence[i] == 'A':
            for j in range(i+1, n):
                if sentence[j] == 'B':
                    cnt += 1

    return cnt

# 문자열에 있는 A를 기준으로 뒤에 있는 B의 개수를 count한 후 k와 비교하기 위해
# 디폴트 문자열을 길이 n만큼 'B'로 채워줌
s = list('B' * n)

# 문자열의 가능한 (i, j) 쌍의 개수가 k와 같기 위한 조합을 만들어야 한다
# 문자열의 길이 안에서 반복을 돌면서 디폴트 문자열의 첫 인덱스부터 A로 채워주면서
# (가능한 쌍의 개수가 k보다 작을 경우 A로 채워주면 'ABBB': 3개 -> 'AABB': 4개)
# 가능한 (i, j) 쌍의 개수를 k와 비교함
# 가능한 (i, j) 쌍의 개수가 k와 같아지면 조건에 부합하는 문자열이 생성되므로 break를 통해 빠져나옴
# 가능한 (i, j) 쌍의 개수가 k보다 클 경우는 다시 'B'로 바꿔준다 ('AABB': 4개 -> 'ABBB': 3개)
for i in range(n):
    s[i] = 'A'
    if check(s) == k:
        break

    elif check(s) > k:
        s[i] = 'B'

# 반례를 생각해야 하는데

# (1) 테스트 케이스의 k값이 0일 경우를 먼저 고려
# 'ABBB': 3개 > k=0 -> 'BABB': 2개 > k=0 -> 'BBAB': 1개 > k=0 -> 'BBBA': 0개 = k=0
# 따라서 위의 반복문에서 'BBBA'가 반환되므로 반례로 고려하지 않아도 됨

# (2) 문자열 길이 n 안에서 가능한 (i, j) 쌍의 개수 최대 값 < k일 경우
# n=6, k=10
# 'AAABBB'일 경우 3x3=9개로 최대인데 k = 10 -> 위의 반복문이 끝나면 'AAAAAA'로 반환되있음
# 따라서 가능한 문자열이 존재하지 않기 때문에 -1로 출력해준다
s = ''.join(s)
if s == 'A' * n:
    print(-1)

else:
    print(s)






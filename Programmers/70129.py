def solution(x):
    answer = []

    trans_cnt = 0 # 이진 변환 횟수
    zero_cnt = 0 # 0을 지운 총 횟수

    while True:
        if x == '1':
            break
        zero_cnt += x.count('0') # 지운 0의 개수 count
        x = x.replace('0', '') # 0 제거

        x = bin(len(x))[2:] # 0을 제거 한 후 문자열 길이 이진 변환

        trans_cnt += 1 # 이진 변환 count

    answer = [trans_cnt, zero_cnt]

    return answer
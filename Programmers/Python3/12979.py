# 기지국 설치
def solution(n, stations, w):
    answer = 0
    cur = 1
    idx = 0
    while cur <= n:
# 설치된 전파에 닿지 않는 위치라면
        if idx >= len(stations) or cur < stations[idx] - w:
            cur += 2 * w + 1
            answer += 1
        else:
            cur = stations[idx] + w+ 1
            idx += 1        
    return answer
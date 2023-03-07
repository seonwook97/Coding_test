# 더 맵게
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        try:
            min = heapq.heappop(scoville)
            heapq.heappush(scoville, min + 2 * heapq.heappop(scoville))
            answer += 1

        except IndexError:
            return -1
    return answer




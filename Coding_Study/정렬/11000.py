import sys
import heapq
input = sys.stdin.readline

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
# 수업 시작시간을 기준으로 오름차순
# -> 시작시간이 가장 최소인것부터 탐색해야 강의실 하나의 마지막 수업이 끝나는 시각을 기준으로 다음 강의실 수업도 배정
# -> 최소의 강의실만을 사용
time_table.sort()
heap = []
heapq.heappush(heap, time_table[0][1])
for i in range(1, n):
    if heap[0] <= time_table[i][0]: # 전 수업의 끝나는 시작이 다음 회의의 시작시간보다 작거나 같으면 다음 수업의 끝나는 시각만을 큐에 남겨 한 강의실로 묶음
        heapq.heappop(heap)
    heapq.heappush(heap, time_table[i][1])
# print(heap)
print(len(heap))

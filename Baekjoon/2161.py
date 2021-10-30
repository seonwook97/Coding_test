# 메모리: 34288KB, 시간: 116ms
import sys
import queue
input = sys.stdin.readline

n = int(input())
queue = queue.Queue()
for i in range(1, n + 1):
    queue.put(i)

while queue.qsize() > 1:
    print(queue.get(), end=' ')
    queue.put(queue.get())

print(queue.get())






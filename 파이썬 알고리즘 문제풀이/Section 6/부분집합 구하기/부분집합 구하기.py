import math
import time
import sys
# sys.stdin = open('in1.txt', 'rt')
# 실행시간 체크
# start = time.time()

# code
def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()

    else:
        ch[v] = 1
        DFS(v+1)

        ch[v] = 0
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)
    

# end = time.time()
# print(f"{end - start:.5f} sec")
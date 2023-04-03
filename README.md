# 알고리즘 정리 by GPT-3.5
## 목차
- [이진 탐색(Binary Search): O(log n)](#이진-탐색binary-search-o-log-n)
- [버블 정렬(Bubble Sort): O(n^2)](#버블-정렬bubble-sort-o-n2)
- [선택 정렬(Selection Sort): O(n^2)](#선택-정렬selection-sort-o-n2)
- [삽입 정렬(Insertion Sort): O(n^2)](#삽입-정렬insertion-sort-o-n2)
- [퀵 정렬(Quick Sort): O(n log n) (worst case: O(n^2))](#퀵-정렬quick-sort-on-log-n-worst-case-on2)
- [합병 정렬(Merge Sort): O(n log n)](#합병-정렬merge-sort-o-n-log-n)
- [깊이 우선 탐색(DFS): O(V + E)](#깊이-우선-탐색dfs-ov--e-v-정점-수-e-간선-수)
- [너비 우선 탐색(BFS): O(V + E)](#너비-우선-탐색bfs-ov--e-v-정점-수-e-간선-수)
- [최소 신장 트리(Kruskal's Algorithm): O(E log V)](#최소-신장-트리kruskals-algorithm-o-e-log-v)
- [다익스트라 알고리즘(Dijkstra's Algorithm): O(E log V)](#다익스트라-알고리즘dijkstras-algorithm-o-e-log-v-e-간선-수-v-정점-수)
- [플로이드-와샬 알고리즘(Floyd-Warshall Algorithm): O(V^3)](#플로이드-와샬-알고리즘floyd-warshall-algorithm-o-v3)
- [최대 힙(Max Heap): O(log n)](#최대-힙max-heap-o-log-n-n-heap-size)
- [이항 계수(Binomial Coefficient): O(n^2)](#이항-계수binomial-coefficient-on2)
- [최대 공약수(Greatest Common Divisor): O(log(min(a, b))) ](#최대-공약수greatest-common-divisor-ologmina-b)
- [소수 판별(Prime Check): O(sqrt(n))](#소수-판별prime-check-osqrtn)
- [에라토스테네스의 체(Sieve of Eratosthenes): O(n log log n)](#에라토스테네스의-체sieve-of-eratosthenes-on-log-log-n)
- [다항식 덧셈(Polynomial Addition): O(n)](#다항식-덧셈polynomial-addition-on)
- [부분합(Prefix Sum): O(n)](#부분합prefix-sum-on)
- [투 포인터(Two Pointer): O(n)](#투-포인터two-pointer-on)
- [최장 증가 부분 수열(Longest Increasing Subsequence): O(n log n)](#최장-증가-부분-수열longest-increasing-subsequence-on-log-n)
- [백트래킹(Backtracking)](#백트래킹backtracking)
- [크루스칼 알고리즘(Kruskal's Algorithm) - Union-Find 활용: O(E log V)](#크루스칼-알고리즘kruskals-algorithm---union-find-활용-oe-log-v)
- [이진 탐색 트리(Binary Search Tree): O(log n) (n: 트리 높이)](#이진-탐색-트리binary-search-tree-olog-n-n-트리-높이)
- [트라이(Trie): O(m) (m: 문자열 길이)](#트라이trie-om-문자열-길이)
- [셸 정렬(Shell Sort): O(n log n) ~ O(n^2)](#셸-정렬shell-sort-on-log-n--on2)
- [힙 정렬(Heap Sort): O(n log n)](#힙-정렬heap-sort-on-log-n)
- [랜덤 퀵 정렬(Randomized Quick Sort): O(n log n)](#랜덤-퀵-정렬randomized-quick-sort-on-log-n)
- [수평 직선으로 놓인 선분들의 교차 판정(Bentley-Ottmann Algorithm): O(n log n)](#수평-직선으로-놓인-선분들의-교차-판정bentley-ottmann-algorithm-on-log-n)
- [레드-블랙 트리(Red-Black Tree): O(log n)](#레드-블랙-트리red-black-tree-olog-n)
- [B-트리(B-Tree): O(log n)](#b-트리b-tree-olog-n)
- [해싱(Hashing): O(1) ~ O(n)](#해싱hashing-o1--on)
- [네트워크 플로우(Network Flow)](#네트워크-플로우network-flow)
- [최소 공통 조상(Lowest Common Ancestor, LCA)](#최소-공통-조상lowest-common-ancestor-lca)
- [문자열 매칭(String Matching) - 브루트 포스(Brute Force)](#문자열-매칭string-matching---브루트-포스brute-force)
- [KMP 알고리즘](#kmp-알고리즘)
- [보이어-무어 알고리즘](#보이어-무어-알고리즘)
- [헝가리안 알고리즘(Hungarian Algorithm)](#헝가리안-알고리즘hungarian-algorithm)
- [스패닝 트리(Spanning Tree)](#스패닝-트리spanning-tree)
- [위상 정렬(Topological Sort)](#위상-정렬topological-sort)
- [최소 공통 부분 문자열(LCS)](#최소-공통-부분-문자열lcs)

## 이진 탐색(Binary Search): O(log n)
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 버블 정렬(Bubble Sort): O(n^2)
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

```

## 선택 정렬(Selection Sort): O(n^2)
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

```

## 삽입 정렬(Insertion Sort): O(n^2)
```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

```

## 퀵 정렬(Quick Sort): O(n log n) (worst case: O(n^2))
```python
def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = arr[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    quick_sort(arr, left, j - 1)
    quick_sort(arr, j + 1, right)

```

## 합병 정렬(Merge Sort): O(n log n)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
```

## 깊이 우선 탐색(DFS): O(V + E) (V: 정점 수, E: 간선 수)
```python
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for adjacent_node in graph[node]:
        if not visited[adjacent_node]:
            dfs(graph, adjacent_node, visited)
```

## 너비 우선 탐색(BFS): O(V + E)
```python
from collections import deque

def bfs(graph, start_node):
    visited = [False] * len(graph)
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for adjacent_node in graph[node]:
            if not visited[adjacent_node]:
                visited[adjacent_node] = True
                queue.append(adjacent_node)
```

## 최소 신장 트리(Kruskal's Algorithm): O(E log V)
```python
def kruskal(graph):
    edges = []
    for node in graph:
        for adjacent_node, weight in graph[node]:
            edges.append((weight, node, adjacent_node))
    edges.sort()
    parent = {node: node for node in graph}
    min_spanning_tree = []
    for weight, node1, node2 in edges:
        root1 = find(parent, node1)
        root2 = find(parent, node2)
        if root1 != root2:
            min_spanning_tree.append((node1, node2, weight))
            parent[root2] = root1
    return min_spanning_tree

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]
```

## 다익스트라 알고리즘(Dijkstra's Algorithm): O(E log V) (E: 간선 수, V: 정점 수)
```python
import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    heap = [(0, start_node)]
    while heap:
        curr_distance, curr_node = heapq.heappop(heap)
        if curr_distance > distances[curr_node]:
            continue
        for adjacent_node, weight in graph[curr_node]:
            distance = curr_distance + weight
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                heapq.heappush(heap, (distance, adjacent_node))
    return distances
```

## 플로이드-와샬 알고리즘(Floyd-Warshall Algorithm): O(V^3)
```python
def floyd_warshall(graph):
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(n)]
    for node in graph:
        for adjacent_node, weight in graph[node]:
            distances[node][adjacent_node] = weight
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances
```

## 최대 힙(Max Heap): O(log n) (n: heap size)
```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        max_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return max_item

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)
```

## 이항 계수(Binomial Coefficient): O(n^2)
```python
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]
```

## 최대 공약수(Greatest Common Divisor): O(log(min(a, b)))
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

## 소수 판별(Prime Check): O(sqrt(n))
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## 에라토스테네스의 체(Sieve of Eratosthenes): O(n log log n)
```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```

## 다항식 덧셈(Polynomial Addition): O(n)
```python
class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __add__(self, other):
        m = len(self.coef)
        n = len(other.coef)
        coef = [0] * max(m, n)
        for i in range(m):
            coef[i] += self.coef[i]
        for i in range(n):
            coef[i] += other.coef[i]
        return Polynomial(coef)
```

## 부분합(Prefix Sum): O(n)
```python
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix
```

## 투 포인터(Two Pointer): O(n)
```python
def two_pointer(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return (left, right)
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return None
```

## 최장 증가 부분 수열(Longest Increasing Subsequence): O(n log n)
```python
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

## 백트래킹(Backtracking)
```python
def backtracking(candidates, target):
    def backtrack(start, remain, path):
        if remain == 0:
            result.append(path[:])
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remain - candidates[i], path)
            path.pop()
    result = []
    backtrack(0, target, [])
    return result
```

## 크루스칼 알고리즘(Kruskal's Algorithm) - Union-Find 활용: O(E log V)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True

def kruskal(graph):
    edges = []
    for node in graph:
        for adjacent_node, weight in graph[node]:
            edges.append((weight, node, adjacent_node))
    edges.sort()
    uf = UnionFind(len(graph))
    min_spanning_tree = []
    for weight, node1, node2 in edges:
        if uf.union(node1, node2):
            min_spanning_tree.append((node1, node2, weight))
    return min_spanning_tree
```

## 이진 탐색 트리(Binary Search Tree): O(log n) (n: 트리 높이)
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right

    def search(self, val):
        curr = self.root
        while curr is not None:
            if val == curr.val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False
```

## 트라이(Trie): O(m) (m: 문자열 길이)
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end

    def starts_with(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
```

## 셸 정렬(Shell Sort): O(n log n) ~ O(n^2)
```python
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```

## 힙 정렬(Heap Sort): O(n log n)
```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

## 랜덤 퀵 정렬(Randomized Quick Sort): O(n log n)
```python
import random

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        pivot_index = partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)
    return arr

def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)
    return arr
```

## 수평 직선으로 놓인 선분들의 교차 판정(Bentley-Ottmann Algorithm): O(n log n)
```python
from bisect import bisect_left

class Event:
    def __init__(self, x, type, seg):
        self.x = x
        self.type = type
        self.seg = seg

def intersect(seg1, seg2):
    x1, y1 = seg1[0]
    x2, y2 = seg1[1]
    x3, y3 = seg2[0]
    x4, y4 = seg2[1]
    a, b, c, d = (y2-y1)/(x2-x1), y1-x1*(y2-y1)/(x2-x1), (y4-y3)/(x4-x3), y3-x3*(y4-y3)/(x4-x3)
    if a == c:
        return False
    x = (d - b) / (a - c)
    if x < max(min(x1, x2), min(x3, x4)) or x > min(max(x1, x2), max(x3, x4)):
        return False
    return True

def bentley_ottmann(segs):
    events = []
    for seg in segs:
        if seg[0][0] > seg[1][0]:
            seg[0], seg[1] = seg[1], seg[0]
        events.append(Event(seg[0][0], "left", seg))
        events.append(Event(seg[1][0], "right", seg))
    events.sort(key=lambda event: event.x)

    status = []
    intersections = []
    for event in events:
        if event.type == "left":
            for seg in status:
                if intersect(seg, event.seg):
                    intersections.append((seg, event.seg))
            status.append(event.seg)
            status.sort(key=lambda seg: seg[0][1])
        elif event.type == "right":
            status.remove(event.seg)
    return intersections
```

## 레드-블랙 트리(Red-Black Tree): O(log n)
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = 1  # 1 means red, 0 means black

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 0  # Set color of sentinel node to black
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, val):
        z = Node(val)
        z.left = z.right = z.parent = self.nil
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        z.color = 1
        while z.parent.color == 1:
            if z.parent == z.parent.parent.right:
                y = z.parent.parent.left
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            else:
                y = z.parent.parent.right
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
        self.root.color = 0

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)
```

## B-트리(B-Tree): O(log n)
```python
class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t  # Minimum degree
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.search(k, x.children[i])

    def insert(self, k):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
        else:
            if len(self.root.keys) == 2*self.t - 1:
                new_root = BTreeNode(self.t, False)
                new_root.children.append(self.root)
                self.split_child(new_root, 0, self.root)
                self.root = new_root
            self.insert_non_full(k, self.root)

    def insert_non_full(self, k, x):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == 2*self.t - 1:
                self.split_child(x, i, x.children[i])
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(k, x.children[i])

    def split_child(self, x, i, y):
        z = BTreeNode(y.t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[y.t - 1])
        z.keys = y.keys[y.t:(2*y.t - 1)]
        y.keys = y.keys[0:(y.t - 1)]
        if not y.leaf:
            z.children = y.children[y.t:(2*y.t)]
            y.children = y.children[0:(y.t - 1)]

    def inorder_traversal(self, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys):
            if not x.leaf:
                self.inorder_traversal(x.children[i])
            print(x.keys[i], end=' ')
            i += 1
        if not x.leaf:
            self.inorder_traversal(x.children[i])
```

## 해싱(Hashing): O(1) ~ O(n)
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_val = self._hash_function(key)
        self.table[hash_val].append((key, value))

    def search(self, key):
        hash_val = self._hash_function(key)
        for pair in self.table[hash_val]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        hash_val = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_val]):
            if pair[0] == key:
                del self.table[hash_val][i]
                return True
        return False
```

## 네트워크 플로우(Network Flow)
```python
class FlowNetwork:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u])-1])

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for i, j, k in self.adj[u]:
                if visited[i] == False and j > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = [u, j, k]
        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [[-1, -1, -1] for _ in range(self.V)]
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, parent[s][1])
                s = parent[s][0]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v][0]
                self.adj[u][parent[v][2]][1] -= path_flow
                self.adj[v][parent[v][2]][1] += path_flow
                v = parent[v][0]
        return max_flow
```

## 최소 공통 조상(Lowest Common Ancestor, LCA)
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_lca(root, p, q):
    if not root:
        return None
    if root.val == p or root.val == q:
        return root
    left_lca = find_lca(root.left, p, q)
    right_lca = find_lca(root.right, p, q)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca
```

## 문자열 매칭(String Matching) - 브루트 포스(Brute Force)
```python
def string_matching_brute_force(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1
```

## KMP 알고리즘
```python
def get_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    i, j = 0, 1
    while j < n:
        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1
        elif i > 0:
            i = lps[i-1]
        else:
            lps[j] = 0
            j += 1
    return lps

def string_matching_kmp(text, pattern):
    n, m = len(text), len(pattern)
    lps = get_lps(pattern)
    i, j = 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```

## 보이어-무어 알고리즘
```python
def get_bad_char_table(pattern):
    table = {}
    for i, c in enumerate(pattern):
        table[c] = i
    return table

def get_good_suffix_table(pattern):
    n = len(pattern)
    lps = get_lps(pattern)
    table = [-1] * n
    for i in range(n):
        j = n - lps[n - 1 - i]
        if lps[n - 1 - i] == i + 1:
            j = i + 1
        table[i] = j
    return table

def string_matching_boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    bad_char_table = get_bad_char_table(pattern)
    good_suffix_table = get_good_suffix_table(pattern)
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(good_suffix_table[j], j - bad_char_table.get(text[i], -1))
    return -1
```

## 헝가리안 알고리즘(Hungarian Algorithm)
```python
INF = float('inf')

def hungarian_algorithm(cost_matrix):
    n, m = len(cost_matrix), len(cost_matrix[0])
    label_x = [max(row) for row in cost_matrix]
    label_y = [0] * m
    matching = [-1] * n
    for i in range(n):
        while True:
            visited = [False] * m
            if dfs(i, matching, cost_matrix, label_x, label_y, visited):
                break
            min_diff = INF
            for j in range(n):
                if visited[j]:
                    for k in range(m):
                        if not visited[k]:
                            min_diff = min(min_diff, label_x[j] + label_y[k] - cost_matrix[j][k])
            for j in range(n):
                if visited[j]:
                    label_x[j] -= min_diff
            for k in range(m):
                if visited[k]:
                    label_y[k] += min_diff
    return sum(cost_matrix[i][matching[i]] for i in range(n))

def dfs(i, matching, cost_matrix, label_x, label_y, visited):
    n, m = len(cost_matrix), len(cost_matrix[0])
    for j in range(m):
        if cost_matrix[i][j] == label_x[i] + label_y[j] and not visited[j]:
            visited[j] = True
            if matching[j] == -1 or dfs(matching[j], matching, cost_matrix, label_x, label_y, visited):
                matching[j] = i
                return True
    return False
```

## 스패닝 트리(Spanning Tree)
- Kruskal 알고리즘
```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal_spanning_tree(n, edges):
    disjoint_set = DisjointSet(n)
    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if disjoint_set.union(u, v):
            mst.append((u, v))
    return mst
```
- Prim 알고리즘
```python
import heapq

def prim_spanning_tree(n, edges):
    adj_list = [[] for _ in range(n)]
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    visited = [False] * n
    heap = [(0, 0)] # (distance, node)
    mst = []
    while heap:
        dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if dist > 0:
            mst.append((parent, u))
        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))
    return mst
```

## 위상 정렬(Topological Sort)
- DFS 이용
```python
def dfs_topological_sort(u, adj_list, visited, stack):
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs_topological_sort(v, adj_list, visited, stack)
    stack.append(u)

def topological_sort_dfs(n, edges):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
    visited = [False] * n
    stack = []
    for u in range(n):
        if not visited[u]:
            dfs_topological_sort(u, adj_list, visited, stack)
    return stack[::-1]
```
- Queue 이용
```python
import collections

def topological_sort_queue(n, edges):
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    queue = collections.deque(u for u in range(n) if in_degree[u] == 0)
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return topo_order
```

## 최소 공통 부분 문자열(LCS)
- 동적 계획법(DP) 이용
```python
def lcs_dp(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = ''
    i, j = n1, n2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs
```

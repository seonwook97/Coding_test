# pypy3
import sys
input = sys.stdin.readline
# Union-Find 알고리즘
# 처음의 각각의 원소는 연결된 정보가 없기 때문에 부모로 자기 자신을 가지고 있음
# find(x) 함수: x로 들어온 원소의 Root 노드를 반환
# union(x,y) 함수: y의 Root 노드를 x로 만드는 함수

# 최종 부모 노드를 찾는 것이기 때문에 만약에 어떤 노드 x가 최종 부모 노드가 아니면
# 그 부모 노드 (parent(x))의 부모(find(parent[x]))를 찾는 방법
# Root node를 찾아주는 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

# x와 y의 Root 노드를 찾고,
# Root 노드가 같지 않으면 y의 Root 노드의 부모를 x의 Root 노드로 만들어주는 함수
# 만약 x와 y가 아무 관계가 없었는데, union(x,y)를 하면 x←y의 관계가 성립
# y의 Root 노드가 x의 Root 노드와 같지 않으면
# y의 Root 노드가 x의 Root 노드의 자식이 되도록 하는 함수
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]

test_cases = int(input())

for _ in range(test_cases):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(" ")

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
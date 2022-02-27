# 클린코드
import sys
from collections import defaultdict

input = sys.stdin.readline

tree_count = 0


def solve(board, nutritions, tree_dict, k):
    """
    :param board : 밭
    :param nutritions: 겨울마다 주는 양분
    :param tree_dict: 위치별 나무들의 나이정보
    :param k: 년도
    :return: 남은 나무들의 수
    """
    global tree_count
    num = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    # k년이 흐를때까지
    while num < k:

        # 봄, 여름, 겨울을 한번에 처리해준다
        for i in range(n * n):
            r = i // n
            c = i % n

            nutrition = board[r][c]
            add_nutrition = 0
            trees = tree_dict[(r, c)]

            # 심어진 나무가 없으면 영양분만 공급한다
            if not trees:
                add_nutrition += nutritions[r][c]
                add_nutrition += nutrition
                board[r][c] = add_nutrition
                continue

            cnt = len(trees)
            temp_trees = []
            # 본 & 여름
            while 0 < cnt:
                tree = trees.pop()
                checked = nutrition - tree
                # 양분이 남아 있는지 여부 판단
                if 0 <= checked:
                    # 양분을 먹는다
                    nutrition -= tree
                    # 나이를 증가시키고, 임시 배열에 넣어준다
                    temp_trees.append(tree + 1)
                else:
                    # 유효하지 않으므로, 나무 죽이기
                    add_nutrition += (tree // 2)
                    tree_count -= 1
                cnt -= 1
            # 성장한 나무들을 기존 배열에 추가해준다
            trees.extend(temp_trees)

            if 1 < len(trees):
                trees.sort(reverse=True)

            # 겨울 (양분 추가)
            add_nutrition += nutritions[r][c]
            # 남은 양분이 있으면 추가
            add_nutrition += nutrition
            # 보드에 기록
            board[r][c] = add_nutrition

        # 가을
        for key, value in tree_dict.items():
            spread_tree_count = 0
            if len(value) == 0:
                continue

            for i in value:
                # 젤 큰 나무가 5보다도 작으면 패쓰
                if i < 5:
                    break
                if i % 5 == 0:
                    spread_tree_count += 1

            if spread_tree_count > 0:
                r, c = key
            for d in range(8):
                temp_r = r + dr[d]
                temp_c = c + dc[d]
                if 0 <= temp_r < n and 0 <= temp_c < n:
                    # 주변에 나무 번식
                    tree_count += spread_tree_count
                    tree_dict[(temp_r, temp_c)].extend([1] * spread_tree_count)
        # 해를 보낸다
        num += 1
    print(tree_count)
    return tree_count


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nutritions = []
    board = [[5] * n for _ in range(n)]

    for i in range(n):
        nutritions.append(list(map(int, input().split())))

    # 위치를 key로 하는 나무들의 정보를 배열에 저장한다.
    tree_dict = defaultdict(lambda: [])
    for t in range(m):
        r, c, old = map(int, input().strip().split())
        tree_dict[(r - 1, c - 1)].append(old)
        tree_count += 1
    solve(board, nutritions, tree_dict, k)
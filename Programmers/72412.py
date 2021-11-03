# 정확성: O, 효율성: X
def solution(info, query):
    for i in range(len(info)):
        info[i] = list(info[i].split())

    for i in range(len(query)):
        query[i] = query[i].replace('and', '')
        query[i] = list(query[i].split())

    count_list = [0] * len(query)
    for i in range(len(query)):
        for item in info:
            for j in range(5):
                if query[i][j] == '-':
                    continue

                elif j == 4:
                    if int(item[j]) >= int(query[i][j]):
                        count_list[i] += 1

                elif item[j] != query[i][j]:
                    break

    return count_list

# 클린코드
# 정확성: O, 효율성: O
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer

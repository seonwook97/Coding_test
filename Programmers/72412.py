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

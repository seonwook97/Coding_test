def solution(elements):
    sum_set = set()
    cycle = elements * 2
    for i in range(len(elements)):
        for j in range(len(elements)):
            sum_set.add(sum(cycle[i:i+j]))
    return len(sum_set)
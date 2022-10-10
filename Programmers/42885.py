def solution(people, limit):
    people = sorted(people)
    answer = 0
    i = 0 # 가벼운 순 index
    j = len(people) - 1 # 무거운 순 index
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer

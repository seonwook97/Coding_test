def solution(numbers):
    set_sum = set() # list안의 인덱스가 다른 두 개의 숫자를 뽑아서 더한 값들 중 중복값을 피하기 위해 set()으로 일단 반환!
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)): # range의 시작을 i + 1로 해야 뽑힌 순서만 다른 두 숫자의 합에 대한 중복계산을 피한다. 또한 같은 인덱스의 값이 두번 더해지는 것도 피함.
            sum = numbers[i] + numbers[j]
            set_sum.add(sum)

    return sorted(list(set_sum)) # 결과값을 list로 반환해야 하므로 list로 set을 마스킹 한 후 오름차순 정렬을 위해 sorted() 적용.

# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))

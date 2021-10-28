# 메모리: 29452KB, 시간: 68ms
import sys
import itertools as it
input = sys.stdin.readline

while True:
    n_list = list(map(int, input().split()))
    if n_list[0] == 0: # 입력부분 -> 0이 입력되면 입력을 종료
        break
    else:
        n_list.remove(n_list[0]) # list의 첫번째 인덱스 값은 숫자를 입력한 개수 k이므로 제외

    comb_list = list(it.combinations(n_list, 6))

    for comb in comb_list: # combination함수의 반환 값들은 튜플 형태라 출력 형태를 맞춰주기 위해 수정을 해줘야한다.
        print_comb = ''
        for num in comb:
            print_comb += str(num) + ' '
        print(print_comb)
    print()

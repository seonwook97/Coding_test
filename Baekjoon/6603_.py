# 런타임에러 -> 문제를 여러개의 입력값을 한번에 받은 후 한번에 출력하는 것으로 생각하고 풀었었다.
# import sys
# import itertools as it
# input = sys.stdin.readline
# big_list = []

# while True:
#     n_list = list(map(int, input().split()))
#     if n_list[0] == 0: # 입력부분 -> 0이 입력되면 입력을 종료
#         break

#     else: # list의 첫번째 인덱스 값은 숫자를 입력한 개수 k, 첫번째 인덱스를 제외하고 list에 담아줌
#         n_list.remove(n_list[0])
#         big_list.append(n_list) # 입력한 숫자 list를 모두 big_list에 담아줌

# for item_list in big_list: # 입력한 숫자 list를 각각 불러와서 6개 숫자의 조합들을 다시 list에 담아준다 <- 우리가 출력하고자 하는 값
#     comb_list = list(it.combinations(item_list, 6))

#     for comb in comb_list: # combination함수의 반환 값들은 튜플 형태라 출력 형태를 맞춰주기 위해 수정을 해줘야한다.
#         print_comb = ''
#         for num in comb:
#             print_comb += str(num) + ' '
#         print(print_comb)
#     print() # 이어서 입력한 숫자 list에 대한 숫자 6개 조합을 출력하기 전에 개행을 해줌.


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

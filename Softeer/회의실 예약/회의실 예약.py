from collections import defaultdict, Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 회의실종류, m: 회의개수
rm_lst = [input().strip() for _ in range(n)] # 회의실 종류
rsv_dict = defaultdict(list)
for rm in rm_lst:
    rsv_dict[rm] = []

for _ in range(m):
    room, start, end = input().split()
    rsv_dict[room].append([start, end])

able_lst = defaultdict(list)
for key, val in sorted(rsv_dict.items()):
    time_table = ['9', '10', '10', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18']
    for time in val:
        start, end = time[0], time[1]
        time_table.pop(time_table.index(start))
        time_table.pop(time_table.index(end))
  
    for k, v in Counter(time_table).items():
        if v == 1:
            able_lst[key].append(k)

# 출력
prt_cnt = 0
for rm_nm in sorted(rm_lst):
    print('Room {}:'.format(rm_nm))
    if rm_nm not in able_lst.keys():
        print('Not available')

    else:
        print('{} available:'.format(len(able_lst[rm_nm]) // 2))
        # 시간대 출력
        for i in range(0, len(able_lst[rm_nm]), 2):
            if able_lst[rm_nm][i] == '9':
                print('0{}-{}'.format(able_lst[rm_nm][i], able_lst[rm_nm][i+1]))
            
            else:
                print('{}-{}'.format(able_lst[rm_nm][i], able_lst[rm_nm][i+1]))
                
    prt_cnt += 1
    if prt_cnt != len(rm_lst):
        print('-----')
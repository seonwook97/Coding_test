import sys
input = sys.stdin.readline
geer_lst = list(map(int, input().split()))

def check(lst):
    if lst[0] == 1:
        num = 2
        for i in range(1, 8):
            if lst[i] == num:
                num += 1
            
            else:
                return 'mixed'
                break
                
        return 'ascending'
    
    if lst[0] == 8:
        num = 7
        for i in range(1, 8):
            if lst[i] == num:
                num -= 1
            
            else:
                return 'mixed'
                break
        
        return 'descending'
    
    else:
        return 'mixed'

print(check(geer_lst))
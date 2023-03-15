import sys
# sys.stdin = open('in1.txt', 'rt')
n = int(input())
num_list = list(map(int, input().split()))

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True

for num in num_list:
    if isPrime(reverse(num)):
        print(reverse(num), end=' ')
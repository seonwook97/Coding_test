n = int(input())

c = 0
for i in range(1, n+1):
    if i < 100:
        c+=1
    else:
        if (i//100 - i//10%10) == (i//10%10 - i%10):
            c+=1

print(c)

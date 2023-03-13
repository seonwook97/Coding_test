arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
        print(arrMin)

print('최솟값 : {}'.format(arrMin))
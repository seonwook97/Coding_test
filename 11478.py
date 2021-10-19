S = input()
S_part = set()
for i in range(0, len(S)):
    for j in range(0, len(S) - i): # len(S)에서 -i만큼 빼줘야 for문안의 j값이 인덱스 범위를 벗어나지 않고 끝까지 반환하게 된다.
        S_part.add(S[j:j+i+1]) # 쉽게 말해서 "i+1"이 집합 S_part에 반환될 문자열의 "길이"라고 생각하면 된다.

print(len(S_part))



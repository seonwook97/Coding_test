import sys
input = sys.stdin.readline

n = int(input())
word_list = [input().rstrip() for _ in range(n)]

cnt = n
for word in word_list:
    for i in range(0, len(word) - 1):
        # 그룹 단어가 성립하지 않는 조건에 해당하는 단어를 빼줌
        # 앞의 문자가 뒤의 문자열에도 포함되지만 연속된 문자가 아닐 경우
        if word[i] in word[(i + 1):] and word[i] != word[i+1]:
            cnt -= 1
            break # 그룹 단어가 아니므로 다음 단어 확인

print(cnt)
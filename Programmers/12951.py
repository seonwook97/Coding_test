def solution(s):
    s = s.split(' ')
    new_s = []
    for i in range(len(s)):
        temp = []
        for j in range(len(s[i])):
            if j == 0:
                temp.append(s[i][j].upper())

            else:
                temp.append(s[i][j].lower())

        new_s.append(''.join(temp))

    answer = ' '.join(new_s)

    return answer
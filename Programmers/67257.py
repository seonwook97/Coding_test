# expression = "100-200*300-500+20"
def solution(expression):
    operations = [('+', '-', '*'),
                  ('+', '*', '-'),
                  ('-', '+', '*'),
                  ('-', '*', '+'),
                  ('*', '+', '-'),
                  ('*', '-', '+')]

    answer = []
    for op in operations:
        prior_1 = op[0]
        prior_2 = op[1]
        temp_list = []
        for e in expression.split(prior_1):
            temp = ['({})'.format(i) for i in e.split(prior_2)]
            # print(temp)
            temp_list.append('({})'.format(prior_2.join(temp)))
            # print(temp_list)
            # print()
        # print(prior_1.join(temp_list))
        answer.append(abs(eval(prior_1.join(temp_list))))
        # print(answer)
        # print()

    return max(answer)

# print(solution(expression))




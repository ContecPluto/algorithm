memo = [-1]*5000
def factorial(v):
    memo[0], memo[1], memo[2] = 0, 1, 2
    for i in range(3, v+1):
        memo[i] = memo[i-1] * i
    return memo[v]

# print(factorial(6))

import sys
sys.stdin = open('4869.txt', 'r')

T = int(input())
for num in range(1, T+1):
    count = [1]
    check = 1
    N = int(input())
    tape = [1]*(N//10)

    for i in range(N//20):
        # print('i 시작', i)
        tape[i:i+2] = [2]
        # print('시작', tape)
        # print('확인', count)
        # print(len(tape))
        check = factorial(len(tape))
        # print('팩토리아', check)
        if tape.count(1) != 0:
            check = check/(factorial(tape.count(1)) * factorial(tape.count(2)))
        else:
            check = check / factorial(tape.count(2))
        # print('나눈값 ',check)
        check *= 2**tape.count(2)
        # print(2**tape.count(2))
        # print('최종', check)
        count.append(check)
        check = 1
        # count = 1 + 5! / count.1 / count/2 + ...


    print('#{} {}'.format(num, int(sum(count))))

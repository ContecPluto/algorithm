import sys; sys.stdin = open('1222.txt', 'r')

for tc in range(10):
    N = int(input())
    answer = 0
    for i in input():
        if i.isdigit():
            answer += int(i)
    print('#{} {}'.format(tc, answer))
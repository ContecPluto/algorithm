import sys; sys.stdin = open('7701.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    name = sorted(list({input() for _ in range(N)}))
    name.sort(key=len)
    print('#{}'.format(tc))
    print('\n'.join(name))

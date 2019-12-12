import sys; sys.stdin = open('6959.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    winner = 'B'
    while len(arr) != 1:
        arr += (str(int(arr.pop()) + int(arr.pop())))
        # winner = not winner
        if winner == 'A':
            winner = 'B'
        else:
            winner = 'A'
    print('#{} {}'.format(tc, winner))
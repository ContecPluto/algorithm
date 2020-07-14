import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
total = [[0,0] for _ in range(N)]
if N > 1:
    total[0][0], total[0][1], total[1][0], total[1][1] = stairs[0], stairs[0], stairs[1], stairs[0] + stairs[1]

    for i in range(2, N):
        total[i][0] = max(total[i-2]) + stairs[i]
        total[i][1] = total[i-1][0] + stairs[i]
    print(max(total[-1]))
else:
    print(stairs[0])
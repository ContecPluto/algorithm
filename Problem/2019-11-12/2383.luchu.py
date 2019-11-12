import sys; sys.stdin = open('2383.txt', 'r')
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    human, length, max_check = [], [], []
    answer = 0xfffff
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            if arr[j] == 1:
                human.append([i, j])
            elif arr[j] > 1:
                length.append([i, j])
                max_check.append(arr[j])
    length = [[abs(i[0] - j[0]) + abs(i[1] - j[1]) for j in length] for i in human]
    N = len(human)
    for subset in range(1 << N):
        one = [[], []]
        for j in range(N):
            if subset & (1 << j):
                one[0].append(length[j][0])
            else:
                one[1].append(length[j][1])
        midle_check = 0
        for i in range(2):
            one[i] = deque(sorted(one[i]))
        for idx in range(2):
            time = deque()
            time_check = 0
            while one[idx]:
                time_check += 1
                for i in range(len(time)):
                    check = time.popleft()
                    check[1] += 1
                    if check[1] != max_check[idx]:
                        time.append(check)
                if len(time) < 3:
                    for i in range(len(one[idx])):
                        if len(time) >= 3: break
                        if one[idx][0] < time_check:
                            time.append([one[idx].popleft(), 0])
            if time:
                time_check += max_check[idx] - time[-1][1]
            midle_check = max(midle_check, time_check)
            if time_check > answer:
                break
        else:
            answer = midle_check
    print('#{} {}'.format(tc, answer))

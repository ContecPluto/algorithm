import sys; sys.stdin = open('17825.txt', 'r')

ans = 0
def move(history, time, answer, root, clear):
    global ans
    if time == 10:
        ans = max(ans, answer)
        return
    position = [history[0][-1], history[1][-1], history[2][-1], history[3][-1]]
    for i in range(4):
        check = history[i][-1] + arr[time]
        flag = 0
        if clear[i] == 1: continue
        for j in range(4):
            if position[j] == 0: continue
            if i == j: continue
            if clear[j] == 1: continue
            if check == position[j]:
                flag = 1
                break
        if flag == 1: continue
        change = 0
        if root[i] == 0 and check % 5 == 0 and check != 20:
            root[i] = check // 5
            change = 1
        history[i].append(check)

        if check >= arrive[root[i]]:
            clear[i] = 1
            move(history, time + 1, answer, root, clear)
            clear[i] = 0
        else:
            move(history, time + 1, answer + value[root[i]][check], root, clear)

        history[i].pop()
        if change == 1:
            root[i] = 0

        if time == 0:
            return

value = [[], [], [], []]
value[0] = [i for i in range(0, 41, 2)]
value[1] = [i for i in range(0, 10, 2)]
value[1] += [10, 13, 16, 19, 25, 30, 35, 40]
value[2] = [i for i in range(0, 20, 2)]
value[2] += [20, 22, 24, 25, 30, 35, 40]
value[3] = [i for i in range(0, 30, 2)]
value[3] += [30, 28, 27, 26, 25, 30, 35, 40]
arrive = [21, 13, 17, 23]
arr = list(map(int, input().split()))
move([[0], [0], [0], [0]], 0, 0, [0, 0, 0, 0], [0, 0, 0, 0])
print(ans)

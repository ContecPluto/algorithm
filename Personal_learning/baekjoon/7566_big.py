# https://www.acmicpc.net/problem/7568

N = int(input())
humans = []
for val in range(N):
    humans.append(list(map(int, input().split())))

result = ''
for human in humans:
    rank = 1
    for target in humans:
        if human[0] < target[0] and human[1] < target[1]:
            rank += 1
    result += str(rank) + ' '

print(result)
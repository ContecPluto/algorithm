def back(line):
    global result
    if line == N:
        result += 1
        return
    for i in range(N):
        if visit[i]: continue
        for j in range(line-1, -1, -1):
            if line - j == abs(i - chess[j]):
                break
        else:
            chess[line] = i
            visit[i] = True
            back(line + 1)
            visit[i] = False
        if line == 0:
            if i == end:
                break
            answers.append(result)


N = int(input())
chess = [0] * N
visit = [False] * N
result = 0
end = N//2 + 1
answers = []
back(0)


if N == 1:
    print(1)
elif N % 2:
    print(answers[-2] * 2 + answers[-1] - answers[-2])
else:
    print(answers[-2] * 2)

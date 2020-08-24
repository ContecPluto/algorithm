N = int(input())
sequence = [0] + list(map(int, input().split()))
M = int(input())
data = {0: {
    1: 0,
    -1: 0
}}
# print(data[0][1])
for i in range(1, N + 1):
    # print(x)
    # print(data[i-1][1])
    data[i] = {1:0, -1:0}
    data[i][1] = data[i-1][1]
    data[i][-1] = data[i-1][-1]
    data[i][sequence[i]] += 1
    # sequence[i] += sequence[i-1]
# print(sequence)p
print(data)
result = ""
for m in range(M):
    i, j = map(int, input().split())
    # i -= 1
    # j -= 1
    # j -= 1
    # val = sequence[j] - sequence[i]
    # print()
    # val = len(ls) - sum(ls)
    # print(sum(sequence[i:j]))
    # val = 0
    # visit = [False] * N
    # for x in range(i, j):
    #     if visit[x]: continue
    #     for y in range(j):
    #         if x == y or visit[y]: continue
    #         if sequence[x] + sequence[y] == 0:
    #             visit[x], visit[y] = True, True
    #             val += 2
    #             break
    # print(j - i + 1)
    # val = j - i 
    # val = sequence[j] - sequence[i]
    # print(j, i, sequence[j], sequence[i])
    # val = j - i + 1 - sequence[j] + sequence[i-1]
    # result += f"{val}\n"
print(result, end="")

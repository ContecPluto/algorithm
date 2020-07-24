N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
ex_arr = arr[0]
for i in range(1, N):
    if ex_arr[1] <= arr[i][0]:
        cnt += 1
        ex_arr = arr[i]
print(cnt)
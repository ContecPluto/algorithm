

def perm(k, n, used):
    if k == n:
        global result
        check = []
        for i in range(len(order)):
            check.append(order[i])
        result.append(check)

    for i in range(n):
        if used & (1 << i): continue

        order.append(arr[i])

        perm(k + 1, n, used | (1 << i))

        order.pop()


arr = "ABCDEF"

order = []      # 순열 저장
cnt = 1
result =[]
perm(0, len(arr), 0)
print(result)



def perm(k, n, used):
    if k == n:
        global cnt,result
        print("%2d> %s" % (cnt, " ".join(order)))
        cnt += 1
        if order:
            result += [order]
        return

    for i in range(n):
        if used & (1 << i): continue

        order.append(arr[i])

        perm(k + 1, n, used | (1 << i))

        order.pop()


arr = "ABCDE"
order = []      # 순열 저장
cnt = 1
result =[]
perm(0, len(arr), 0)
print(result)

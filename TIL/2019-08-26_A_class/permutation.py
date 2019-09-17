
def perm(z, n):
    global result, memo
    if not memo[n-1]:
        perm(z-1, n-1)

    if not memo[n] and memo[n-1]:
        i = n - 1
        for j in range(len(memo[i])):
            for k in range(len(memo[i][j]) + 1):
                check = memo[i][j].copy()
                check.insert(k, 'D')
                # print(check)
                memo[i + 1].append(check)
        memo[i + 1].sort()
        # result = memo[i+1]
        # print(n)
        # return result
    if z == n:
        result = memo[z]
        return result

    # if k == len(arr):
    #     check = []
    #     for i in range(len(order)):
    #         check.append(order[i])
    #     result.append(check)

    # for i in range(n):
    #     if used & (1 << i): continue
    #     order.append(arr[i])
    #     perm(k + 1, n, used | (1 << i))
    #     order.pop()


arr = "ABCD"
memo = [[] for _ in range(30)]
memo[3] = [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B'], ['C', 'B', 'A']]
# check = []
# # for i in range(1):
# n = 4
# i = n - 4
# for j in range(len(memo[i])):
#     for k in range(len(memo[i][j])+1):
#         check = memo[i][j].copy()
#         check.insert(k, 'D')
#         # print(check)
#         memo[i+1].append(check)
# memo[i+1].sort()

# print(memo[1])


order = []      # 순열 저장
result =[]
perm(5, 5)
print(result)

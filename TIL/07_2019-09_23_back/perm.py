#순열생성
arr = 'ABC'
N = len(arr)
order = [0] * N
visit = [False] * N
def perm(a, k, n):
    if k == n:
        print(a)
    else:
        for i in range(n):
            if visit[i]: continue
            a[k] = i
            visit[i] = True
            perm(a, k+1, n)
            visit[i] = False


perm(order, 0, N)
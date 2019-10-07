import sys; sys.stdin = open('1808.txt', 'r')

def check(k):
    global flag, cnt

    if k == N:
        # print('찾음')
        flag = 1
        cnt[int(X)] = N+1
        return
    for i in arr:
        if i == int(X[k]):
            chose.append(i)
            check(k + 1)



T = int(input())
for tc in range(1):
    print('#', tc+1, end=' ')
    cnt = {}
    flag = 0
    arr = list(map(int, input().split()))
    X = input()
    N = len(X)
    first_check = list(map(int, X))
    length = len(first_check)
    chose = []
    arr = [i for i in range(len(arr)) if arr[i] == 1]
    check(0)
    temp= {}
    for i in arr:
        cnt[i] = 1
    X = int(X)
    arr = set(arr)
    if flag == 0:
        answer = arr.copy()
        for i in answer:
            if i == 0: continue
            temp = list(arr)
            print(arr, i)
            for j in range(len(temp)):
                n = len(str(temp[j]))
                ans = temp[j] * i
                # print(temp[j])
                if 0 < ans <= X and i != 1:
                    cnt[ans] = cnt.get(i) + cnt.get(temp[j]) + 1
                    arr.add(ans)
                ans = (i*(10**n) + temp[j])
                if 0 < ans <= X:
                    cnt[ans] = cnt.get(i) + cnt.get(temp[j])
                    arr.add(ans)
                if temp[j] * i == X or ((i*(10**n)) + temp[j]) == X:
                    # arr += answer
                    cnt[X] += 1
                    flag = 1
                    # print('찾')
                    break


            # arr = list(tuple(arr))
            # arr += answer
            # print(arr, i)





    # print(cnt)
    print(cnt.get(X))
    # print()
    #
    # print(arr)
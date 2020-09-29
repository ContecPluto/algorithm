N = input()
if len(N) > 2:
    N = int(N)
    cnt = 99
    for i in range(100, N+1):
        i = str(i)
        arr = [int(i[j]) - int(i[j-1]) for j in range(1, len(i))]
        val = arr[0]
        for num in arr:
            if val != num:
                break
        else:
            cnt += 1
    print(cnt)
else:
    print(N)
    
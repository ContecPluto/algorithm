def fibo(n):
    if n < len(arr):
        print(arr[n])
    else:
        for i in range(n - len(arr) + 1):
            arr.append(arr[-1] + arr[-2])
        print(arr[n])
    return

arr = [0, 1, 1]
fibo(int(input()))

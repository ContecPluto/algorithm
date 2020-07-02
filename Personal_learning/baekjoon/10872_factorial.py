def factorial(n):
    if n < len(arr):
        print(arr[n])
    else:
        for i in range(n - len(arr) + 1):
            arr.append(arr[-1] * len(arr))
        print(arr[n])
    return


arr = [1, 1, 2, 6]
factorial(int(input()))


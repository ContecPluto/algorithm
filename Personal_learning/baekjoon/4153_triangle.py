while True:
    arr = sorted(list(map(int, input().split())))
    if sum(arr) == 0:
        break
    arr = [i**2 for i in arr]
    x, y, z = arr
    if x + y == z:
        print("right")
    else:
        print("wrong")
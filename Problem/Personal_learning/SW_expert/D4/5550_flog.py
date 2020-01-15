import sys; sys.stdin = open('5550.txt', 'r')
# croak
T = int(input())
index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
for tc in range(1, T + 1):
    flog = input()
    arr = [0]
    for i in flog:
        if i == 'c':
            for j in range(len(arr)):
                if arr[j] == 0:
                    arr[j] = 1
                    break
            else:
                arr.append(1)
        else:
            idx = index.get(i)
            for j in range(len(arr)):
                if arr[j] == idx:
                    arr[j] = 0 if arr[j] == 4 else arr[j] + 1
                    break
            else:
                arr[0] = 99
                break
    print('#{} {}'.format(tc, -1 if sum(arr) != 0 else len(arr)))
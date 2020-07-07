def calculation(n, result, plus, minus, multi, div):
    global max_val, min_val
    if n == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    if plus:
        calculation(n + 1, result + numbers[n], plus - 1, minus, multi, div)
    if minus:
        calculation(n + 1, result - numbers[n], plus, minus - 1, multi, div)
    if multi:
        calculation(n + 1, result * numbers[n], plus, minus, multi - 1, div)
    if div:
        calculation(n + 1, int(result / numbers[n]), plus, minus, multi, div - 1)
    return


N = int(input())
numbers = list(map(int, input().split(' ')))
max_val = -0xffffffff
min_val = 0xffffffff
opers = list(map(int, input().split(' ')))
calculation(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
print(max_val)
print(min_val)
import sys

def factorial(n):
    if len(facto) > n:
        return facto[n]
    else:
        for i in range(n - len(facto) + 1):
            facto.append((facto[-1]+facto[-2]) % 15746)
        return facto[n]


N = int(sys.stdin.readline())
facto = [0, 1, 2, 3, 5]
print(factorial(N))

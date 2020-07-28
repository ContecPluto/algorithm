from math import sqrt

N = int(input())
M = int(input())
if N == 1:
    N += 1

result = []
for number in range(N, M + 1):
    if number % 2 or number == 2:
        for i in range(3, int(sqrt(number)) + 1, 2):
            if not number % i:
                break
        else:
            result.append(number)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
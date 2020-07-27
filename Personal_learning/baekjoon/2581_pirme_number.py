N = int(input())
M = int(input())

result = []
for number in range(N, M + 1):
    if number != 1 and number % 2 != 0 or number == 2:
        for i in range(3, number//2, 2):
            if number % i == 0:
                break
        else:
            result.append(number)
            
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
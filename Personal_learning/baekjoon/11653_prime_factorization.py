N = int(input())
result = []
num = 2
while not N % num:
    N //= num
    result.append(num)
  
num = 3
while num**2 <= N:
    while not N % num:
        N //= num
        result.append(num)
    num += 2
    
if N != 1:
    result.append(N)
print(*result, sep="\n")
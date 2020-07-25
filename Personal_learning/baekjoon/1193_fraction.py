N = int(input())
num = [0]
plus_num = 0

while num[-1] < N:
    plus_num += 1
    num.append(num[-1] + plus_num)
N = num[-1] - N
if plus_num%2:
    print("{}/{}".format(1 + N, plus_num - N))
else:    
    print("{}/{}".format(plus_num - N, 1 + N))
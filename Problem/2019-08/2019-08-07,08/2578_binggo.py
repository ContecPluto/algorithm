import sys
sys.stdin = open('2578.txt', 'r')

binggo = []         #
mc = []
count = [0]*25
x_bin, y_bin, cross, cross2 =0, 0, 0, 0
n_count = 0
b_count = 0


# for i in range(25):
#     count[i] += 1*i
# print(count[4:24:4])

for _ in range(5):
    binggo += list(map(int, input().split()))
for _ in range(5):
    mc += list(map(int, input().split()))


# print('시작')
for idx, number in enumerate(mc):
    n_count += 1
    count[binggo.index(number)] += 1
    # print(count)
    for i in range(5):
        # print(i)
        if sum(count[i*5:i*5+5]) == 5:
            # print('x축', count[i*5:i*5+5])
            b_count += 1
        if sum(count[i::5]) == 5:
            # print('y축')
            b_count += 1
    if sum(count[::6]) == 5:
        # print('대각선1')
        b_count += 1
    if sum(count[4:len(binggo)-1:4]) == 5:
        # print('대각선2')
        b_count += 1
    if b_count >= 3:        
        print(n_count)
        break
    # print('끝')
    b_count = 0
    


    



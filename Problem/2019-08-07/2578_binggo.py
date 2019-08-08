import sys
sys.stdin = open('2578.txt', 'r')
binggo = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
count = [[0]*5 for _ in range(5)]
x_bin,y_bin, cross, cross2 =0,0,0,0
n_count = 0
b_count = 0

for i in range(len(binggo)):
    for j in range(len(binggo[0])):
        n_count += 1
        # print(mc[i][j])
        for k in range(len(binggo)):
            if mc[i][j] in binggo[k]:
                # print(mc[i][j], binggo[k].index(mc[i][j]))
                count[k][binggo[k].index(mc[i][j])] += 1                
                break 

        for x in range(5):
            cross += count[x][x]
            cross2 += count[x][4-x]
            for y in range(5):
                x_bin += count[x][y]
                y_bin += count[y][x]
            if x_bin == 5:
                b_count += 1
            if y_bin == 5:
                b_count += 1
            x_bin, y_bin = 0, 0
        if cross == 5:
            b_count +=1
        if cross2 == 5:
            b_count +=1
        cross,cross2 = 0, 0    


print(b_count)


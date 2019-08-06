import sys
sys.stdin = open('4836.txt', 'r')

T = int(input())
for i in range(1, T+1):
    count = [[0 for _ in range(10)] for _ in range(10)]
    r_num = int(input())
    racs = [list(map(int, input().split())) for _ in range(r_num)]
    count_n=0
    # print(racs)
    
 
    for rac in racs:
        for x in range(rac[0],rac[2]+1):
            for y in range(rac[1],rac[3]+1):
                count[x][y] += rac[4]

    for x in range(len(count)):
        for y in range(len(count[0])):
            if count[x][y] > 2 :
                count_n += 1


    print('#{} {}'.format(i, count_n))
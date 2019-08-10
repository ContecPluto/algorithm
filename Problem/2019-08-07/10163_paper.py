import sys
sys.stdin = open('10163.txt', 'r')

T=int(input())
paper = [list(map(int,input().split())) for _ in range(T)]
answer = 0
result = [[0 for _ in range(0,101)] for _ in range(0,101)]   


for idx, i in enumerate(paper):
    for x in range(i[0],i[0]+i[2]):
        for y in range(i[1],i[0]+i[3]):
            # print(x,y)
            result[x][y] = idx+1

for j in range(T):
    for i in range(len(result)):
        answer += result[i].count(j+1)
    print(answer) 
    answer=0
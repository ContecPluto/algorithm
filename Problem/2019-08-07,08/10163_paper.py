import sys
sys.stdin = open('10163.txt', 'r')

T = int(input())
paper = [list(map(int, input().split())) for _ in range(T)]
answer = [0]*T
result = [[0 for _ in range(0, 101)] for _ in range(0, 101)]


for idx, i in enumerate(paper):
    for x in range(i[0], i[0]+i[2]):
        for y in range(i[1], i[1]+i[3]):
            result[x][y] = idx+1

for x in range(len(result)):
    for y in range(len(result)):
        if result[x][y] != 0:
            answer[result[x][y]-1] += 1
for i in answer:
    print(i)

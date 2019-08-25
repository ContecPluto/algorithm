import sys; sys.stdin = open('2628.txt', 'r')

x, y = list(map(int, input().split()))
paper = [[1 for _ in range(y)] for __ in range(x)]
cut_list = [[0,y], [0,x]]
horizontal = 0
vertical = 0

cut_number = int(input())
for i in range(cut_number):
    cut = list(map(int, input().split()))
    if cut[0] == 1:
        cut_list[1].append(cut[1])
    if cut[0] == 0:
        cut_list[0].append(cut[1])
for i in range(2):
    cut_list[i].sort()

for i in range(len(cut_list[0])-1):
    vertical = max(vertical, cut_list[0][i+1] - cut_list[0][i])
for i in range(len(cut_list[1])-1):
    horizontal = max(horizontal, cut_list[1][i+1] - cut_list[1][i])
print(vertical*horizontal)

        
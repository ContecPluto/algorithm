# # https://www.acmicpc.net/problem/11729

def hanoi(n):
    global result
    if sum(arr[2]) == sum_tower:
        return
    idx = -1
    for i in range(1, N+1):
        for j in range(3):
            if arr[j][-1] == i:
                idx = j
                break
        else:
            continue
        move_num = idx
        for j in range(2):
            move_num += move
            if move_num == -1:
                move_num = 2
            if move_num == 3:
                move_num = 0 
            if arr[idx][-1] < arr[move_num][-1]:
                arr[move_num].append(arr[idx].pop())
                memory.append([idx+1, move_num+1])
                break
    hanoi(n)                 


N = int(input())
move = 1 if N % 2 == 0 else -1
arr = [list(range(N, 0, -1)), [N+1], [N+1]]
arr[0].insert(0, N+1)
sum_tower = sum(arr[0])
result = 0xffff
memory = []
hanoi(0)

print(len(memory))
for line in memory:
    print(*line)

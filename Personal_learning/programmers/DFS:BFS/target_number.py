answer = 0

def DFS(numbers, target, k, num):
    global answer
    if k == len(numbers):
        if num == target:
            answer += 1
        return
    DFS(numbers, target, k+1, num + numbers[k])
    DFS(numbers, target, k+1, num - numbers[k])

def solution(numbers, target):
    DFS(numbers, target, 0, 0)
    print(answer)
    return answer
    
solution([1, 1, 1, 1, 1], 3)
def solution(brown, yellow):
    answer = []
    N = brown // 2
    for i in range(3, N):
        for j in range(3, i+1):
            x = i*2 + j*2 - 4
            y = (i-2) * (j-2)
            if x == brown and y == yellow:
                return [i, j]
    return [0, 0]

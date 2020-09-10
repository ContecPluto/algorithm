def solution(board, moves):
    answer = 0
    basket = [0]
    for move in moves:
        move -= 1
        for idx in range(len(board)):    
            dole = board[idx][move]
            if dole:
                if dole == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(dole)
                board[idx][move] = 0
                break
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
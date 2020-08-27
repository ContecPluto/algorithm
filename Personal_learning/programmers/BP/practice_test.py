def solution(answers):
    answer = []
    cnts = [0, 0, 0]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    pattern_length = [5, 8, 10]

    for idx, ans in enumerate(answers):
        for p_idx in range(3):
            if pattern[p_idx][idx%pattern_length[p_idx]] == ans:
                cnts[p_idx] += 1

    max_cnt = max(cnts)
    for c_idx in range(3):
        if cnts[c_idx] == max_cnt:
            answer.append(c_idx+1)

    return answer

print(solution([1, 2, 3, 4, 5]))
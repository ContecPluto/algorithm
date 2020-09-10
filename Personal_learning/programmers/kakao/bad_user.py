answer = set()

def DFS(user_id, banned_id, s, arr, indices):
    global answer
    if s == len(banned_id):
        answer.add(tuple(sorted(arr)))
        return 
        
    for user_idx in range(len(user_id)):
        user = list(user_id[user_idx])
        user_str = user_id[user_idx]
        if len(user) == len(banned_id[s]):
            for idx in indices[s]:
                user[idx] = "*"

            if user == banned_id[s] and user_str not in arr:
                arr.append(user_str)
                DFS(user_id, banned_id, s+1, arr, indices)
                arr.pop()



def solution(user_id, banned_id):
    global answer
    indices = [[j for j in range(len(banned_id[s])) if banned_id[s][j] == "*"] for s in range(len(banned_id))]
    banned_id = list(map(list, banned_id))
    # user_id = list(map(list, user_id))
    answer = set()
    DFS(user_id, banned_id, 0, [], indices)
    return len(answer)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
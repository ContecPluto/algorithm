answer = 0xfffff

def DFS(begin, target, words, string, visit, cnt):
    global answer
    if cnt >= answer:
        return

    if "".join(string) == target:
        answer = cnt
        return

    N = len(begin)
    for word_idx in range(len(words)):
        word = words[word_idx]
        origin_word = string[::]
        wrong = 0
        c_idx = 0
        for idx in range(N):
            if word[idx] != string[idx]:
                c_idx = idx
                wrong += 1

        if wrong == 1 and not visit[word_idx]:
            string[c_idx] = word[c_idx]
            visit[word_idx] = True
            DFS(begin, target, words, string, visit, cnt+1)
            visit[word_idx] = False
            string[c_idx] = origin_word[c_idx]
            

def solution(begin, target, words):
    global answer
    if target in words:
        answer = 0xfffff
        DFS(begin, target, words, list(begin), [False] * len(words), 0)
        if answer == 0xfffff:
            answer = 0
        return answer
    else:
        return 0


# print(solution("para", "dota", ["bara", "bora", "dora", "dota"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

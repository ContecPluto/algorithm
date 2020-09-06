answer = []

def DFS(s, tickets, visit, route):
    global answer
    if len(route) == len(tickets)+1:
        answer = route
        return

    if answer:
        return

    for idx in range(len(tickets)):
        a, b = tickets[idx]
        if a == s:
            if visit[idx] == False:
                visit[idx] = True
                DFS(b, tickets, visit, route+[b])
                visit[idx] = False

def solution(tickets):
    global answer
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    answer = []
    N = len(tickets) + 1
    visit = [False] * len(tickets)
    DFS("ICN", tickets, visit, ["ICN"])
    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
from heapq import heappop, heappush

def solution(tickets):
    air_route = {}
    tickets = sorted(tickets, key=lambda x: x[0])
    Q = []
    answer = []
    N = len(tickets) + 1

    for a, b in tickets:
        heappush(Q, [a, [a]])
        if air_route.get(a) == None:
            air_route[a] = [b]
        else:
            air_route[a].append(b)
            air_route[a] = sorted(air_route[a])
    print(air_route)


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
import sys
input = sys.stdin.readline

N = int(input())
result = ""
for i in range(N):
    scores = list(map(int, input().split()))
    if scores[0] <= 1:
        result += "%.3f"%0 + "%\n"
    else:
        scores = scores[1:]
        average = sum(scores)/len(scores)
        cnt = 0
        for score in scores:
            if score > average:
                cnt += 1
        result += "%.3f"%(cnt/len(scores) * 100) + "%\n"
print(result, end="")
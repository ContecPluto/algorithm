import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    return list(answer.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
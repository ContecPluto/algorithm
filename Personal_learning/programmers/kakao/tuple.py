def solution(s):
    a = ""
    tuple_arr = []
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    for i in s1:
        tuple_arr.append(set(map(int, i.split(','))))

    tuple_arr.sort(key=lambda x: len(x))
    answer = list(tuple_arr[0])

    for idx in range(1, len(tuple_arr)):
        for i in tuple_arr[idx] - tuple_arr[idx-1]:
            answer.append(i)
    return answer

print(solution("{{20,111},{111}}"))
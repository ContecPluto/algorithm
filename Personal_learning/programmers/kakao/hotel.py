def solution(k, room_number):
    answer = []
    room_dict = {}
    for number in room_number:
        num = number
        visit = [number]

        while num in room_dict:
            num = room_dict[num]
            visit.append(num)

        answer.append(num)
        num += 1
    
        for room in visit:
            room_dict[room] = num
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1, 10]))
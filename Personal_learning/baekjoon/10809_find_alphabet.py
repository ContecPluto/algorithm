# answer = [-1] * 26
# words = input()

# for x in range(len(words)):
#     idx = ord(words[x]) - 97
#     if answer[idx] == -1:
#         answer[idx] = x
        
# print(*answer, sep=' ', end='\n')

alphabet = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), range(26)))
answer = [-1] * 26
words = input()
for x in range(len(words)):
    idx = alphabet[words[x]]
    if answer[idx] == -1:
        answer[idx] = x
        
print(*answer, sep=' ', end='\n')
import sys
sys.stdin = open('7675.txt', 'r')
T = int(input())

for num in range(T):
    sentence_count = input()
    Conversation = input()
    sentence = ''
    cs = []
    cs_cheak=[]

    for word in Conversation:
        if word in ('.', '?', '!'):
            cs.append(sentence)
            sentence = '' 
        else:
            sentence+=word
    count = [0]*len(cs)
    # print(cs)

    for i in range(len(cs)):
        cs_cheak = cs[i].split(' ')
        print(cs_cheak)
        for j in range(len(cs_cheak)):
            if cs_cheak[j].istitle():
                if len(cs_cheak[j])==1 and cs_cheak[j].isupper():
                    # print('한글자만 출력 여기서 나오면 안됨', cs_cheak[j])
                    count[i] += 1
                # print(cs_cheak[j])
                elif cs_cheak[j][-1:].islower():
                #    print('체크되는 이름',cs_cheak[j])
                   count[i] += 1
                #    print(count, cs_cheak[j])
    print('#{} {}'.format(num+1,' '.join(map(str,count))))
import sys; sys.stdin = open('4047.txt','r')


T = int(input())
kind_card = ['S', 'D', 'H', 'C']

for tc in range(1, T+1):
    kind_card_counting = [13] * 4
    card = input()
    check = [[] for _ in range(4)]


    for i in range(0, len(card), 3):
        if int(card[i + 1] + card[i + 2]) not in check[kind_card.index(card[i])]:
            check[kind_card.index(card[i])].append(int(card[i + 1] + card[i + 2]))
            kind_card_counting[kind_card.index(card[i])] -= 1
        else:
            print('#{} ERROR'.format(tc))
            break
    else:
        print('#{} {}'.format(tc, ' '.join(map(str, kind_card_counting))))



import sys 

input = sys.stdin.readline

N , M = map(int, input().split(' '))
card_list = []
card_list.extend(list(map(int, input().split(' '))))

result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            #print(i,j,k)
            #print(card_list)
            if card_list[i] + card_list[j] + card_list[k] > M:
                continue
            else:
                result = max(result,card_list[i] + card_list[j] + card_list[k])

print(result)
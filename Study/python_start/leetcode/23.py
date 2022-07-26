import heapq
input_lst = [
    '1->4->5',
    '1->3->4',
    '2->6'
]
result_lst =[]
final = []
for list in input_lst:
    temp_lst = list.split('->')
    for temp in temp_lst:
        heapq.heappush(result_lst, temp)
while result_lst:
    print(str(heapq.heappop(result_lst)) ,end='')
    if result_lst:
        print('->',end='')

import sys 
import statistics

input = sys.stdin.readline

cnt = int(input())
lst = []
for i in range(cnt):
    val = int(input())
    lst.append(val)
lst.sort()

#counted_lst = list(Counter(lst).most_common())

#counted_lst_number = [counted_lst[i][1] for i in range(len(counted_lst))]

print(round(sum(lst)/cnt))

print(lst[int(cnt/2)])

mode = statistics.multimode(lst)
mode.sort()
print(mode[1] if len(mode) > 1 else mode[0])

print(max(lst)- min(lst))
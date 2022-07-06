import sys ,math 
N,M, K = map(int, input().split(' '))
h = math.ceil(math.log2(N)) #높이 지정 
tree_size = 1 << (h+1)
tree = [0] * tree_size
# tree = [0 for _ in range(2**math.ceil(math.log2(N // 2)))]
# lst = [i+1 for i in range(N)]
lst = []
for i in range(N):
    lst.append(int(input()))
# print(lst)
def init(lst,node,tree,start, end):
    if start == end:
        # print("same",node,start,end)
        tree[node] = lst[start] # 실제 입력값들 초기 저장 
    elif 2*node+1 < len(tree):
        # print(node,start,end)
        init(lst, 2*node, tree, start, (start+end)//2)
        init(lst, 2*node+1, tree, (start+end)//2+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]

def get_interval_sum(node, tree, left, right, start ,end):
    if left > end or right < start:
        return 0 
    if left <= start and end <= right:
        return tree[node]
    lnum = get_interval_sum(2*node, tree, left, right, start, (start+end)//2)
    rnum = get_interval_sum(2*node+1, tree, left, right, (start+end)//2+1, end)
    return lnum + rnum 
def update(node, tree, val, index, start, end):
    while True:
        if (index ==start) and (index == end) and (start <= end):
            break
        # print(start, end, node)
        mid = (start+end)//2
        if index <= mid:
            end = mid 
            node *=2
        else:
            start = mid+1
            node = node*2 +1
            
    # print('2',start, end, node)
    if index == start or index== end:
        diff = val - tree[node]
        tree[node] = val 
        while node > 1:
            node //= 2
            tree[node] += diff 
        return tree   
init(lst, 1,tree, 0, N-1)
# print(tree)
# print(len(tree))
# print(get_interval_sum(1, tree, 3, 6, 0, N-1))
# update(tree, 20, 11)
# print(len(tree))
# print(tree[6], tree[12])
for i in range(M+K):
    a, b, c = map(int, input().split(' '))
    # print("1",tree)
    if a == 1:
        tree = update(1,tree, c, b-1, 0, N-1)
    elif a ==2:
        print(get_interval_sum(1, tree,b-1,c-1,0, N-1))

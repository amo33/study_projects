# https://cocoon1787.tistory.com/433
import sys , math 
from collections import deque 
N, k = map(int, input().split(' '))
visited = [0 for _ in range(N+1)]
h = math.floor(math.log2(N))
tree_size = 1 << (h+2) 
print(tree_size)
tree = [0] * (tree_size)
# tree = [0] * (tree_size*2-1) 
lst = [i+1 for i in range(N)]
def init(node, tree, lst,start, end,size_tree):
    if start == end:
        tree[node] = 1 
    elif 2*node +1 < size_tree:
        print(tree)
        init(2*node, tree, lst, start, (start+end)//2, size_tree)
        init(2*node+1, tree, lst, (start+end)//2+1, end, size_tree)
        tree[node] = tree[2*node] + tree[2*node +1]
def query(node, tree, index, start ,end):
    if start == end:
        return start # 번호 받기 
    mid = (start+end)//2
    # print(mid, start, end)
    if 2*node < len(tree) and index < mid:
        return query(2*node, tree, index, start, mid)
    elif  2*node+1 < len(tree) and index > mid:
        return query(2*node+1, tree, index - tree[2*node],mid + 1 , end)
    elif index == mid:
        return mid
init(1, tree, lst,0, N-1, len(tree))
print(tree)
def update(node, tree, start, end, del_num ):
    tree[node] -= 1
    if start == end:
        return 
    mid = (start+end)//2
    if del_num <= mid:
        update(2*node, tree, start, mid, del_num )
    else:
        update(2*node+1, tree,mid + 1 , end, del_num)
index = 0
for i in range(N):

    size = N - i 
    # if index != 0:
    #     index += k
    # else: 
    index += k -1 
    if index % size == 0:
        index = size 
    else:
        index %= size 
    # print(index, size)
    num = query(1, tree, index, 0, N-1)
    # print(num)
    print(i, num)
    update(1, tree ,0, N-1, num)
    print(tree)
# def update(node, tree, index, ):

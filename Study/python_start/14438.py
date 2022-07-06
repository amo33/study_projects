import sys ,math 
# N,M, K = map(int, input().split(' '))
N = int(input())
h = math.ceil(math.log2(N)) #높이 지정 
tree_size = 1 << (h+1)
tree = [0] * tree_size

# lst = [i+1 for i in range(N)]
lst = list(map(int,sys.stdin.readline().split(' ')))
# print(lst)
def init(lst,node,tree,start, end):
    if start == end:
        # print("same",node,start,end)
        tree[node] = lst[start] # 실제 입력값들 초기 저장 
    elif 2*node+1 < len(tree):
        # print(node,start,end)
        init(lst, 2*node, tree, start, (start+end)//2)
        init(lst, 2*node+1, tree, (start+end)//2+1, end)
        tree[node] = min(tree[2*node] , tree[2*node+1])

def get_interval_min(node, tree, left, right, start ,end):
    if left > end or right < start:
        return -1 
    if left <= start and end <= right:
        return tree[node]
    lnum = get_interval_min(2*node, tree, left, right, start, (start+end)//2)
    rnum = get_interval_min(2*node+1, tree, left, right, (start+end)//2+1, end)
    if lnum == -1:
        return rnum 
    elif rnum == -1:
        return lnum 
    else:
        return min(lnum, rnum)
def update(node, tree, val, index, start, end): # 재귀로 구현하자..
    if index < start or index > end:
        return
    if start == end:
        #a[index] = val
        tree[node] = val
        return
    update(node*2, tree, val, index,start, (start+end)//2)
    update(node*2+1, tree,val, index,(start+end)//2+1, end)
    tree[node] = min(tree[node*2], tree[node*2+1])
# print(lst)
init(lst, 1,tree, 0, N-1)
M = int(input())
for i in range(M):
    a, b, c = map(int, input().split(' '))
    # print("1",tree)
    if a == 1:
        update(1,tree, c, b-1, 0, N-1)
    elif a ==2:
        print(get_interval_min(1, tree,b-1,c-1,0, N-1))

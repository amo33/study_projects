import sys

def preorder(tree,index):
    print(tree[index][0],end="")
    if tree[index][1] != '.':
        preorder(tree,tree[index][1])
    if tree[index][2] != '.':
        preorder(tree, tree[index][2])

def postorder(tree, index):
    if tree[index][1] != '.':
        postorder(tree, tree[index][1])
    if tree[index][2] != '.':
        postorder(tree, tree[index][2])
    print(tree[index][0],end="")
    
def inorder(tree, index):
    
    if tree[index][1] != '.':
        inorder(tree, tree[index][1])
    print(tree[index][0],end="")
    if tree[index][2] != '.':
        inorder(tree, tree[index][2])
n = int(sys.stdin.readline())
    
matrix ={}
# matrix.append([0])
for i in range(n):
    temp_lst=list(map(str, input().split()))
    matrix[temp_lst[0]] = temp_lst
# print(matrix)
preorder(matrix, "A")
print()
inorder(matrix,"A")
print()
postorder(matrix,"A")


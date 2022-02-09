import sys

input = sys.stdin.readline

def preorder(node, matrix):
    print(1)
    if check[node] != 1:
        print(matrix[node][0])
        check[node] = 1
        left_token = matrix[node][1]
        if left_token != '.':
            matrix[node][1] = '0'
            lflag = 1
        else:
            lflag = 0
        
        right_token = matrix[node][2]
        if right_token != '.':
            rflag = 1
            matrix[node][2] = '0'
        else:
            rflag = 0
        for index, lst in enumerate(matrix):
            if left_token in lst & lflag == 1:
                left_key = index #+ lst.index(left_token)
            elif right_token in lst & rflag == 1:
                right_key = index #+ lst.index(right_token)
        preorder(left_key, matrix)
        preorder(right_key, matrix)




n = int(sys.stdin.readline())

matrix =[[] for _ in range(n)]
check = [0] * n
for i in range(n):
    matrix[i].append((map(str, input().split())))
print(matrix)
preorder(0, matrix)

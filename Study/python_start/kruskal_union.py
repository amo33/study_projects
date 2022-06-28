import sys 

N = int(input())
M = int(input())
parent_lst = [i for i in range(N+1)]
print(parent_lst)
distance_lst = []
class nodeinfo:
    def __init__(self, start, end, distance):
        self.a = start 
        self.b = end 
        self.dist = distance
        #self.union(self.a,self.b) # 서로는 추가 
    def get_parent(self, node):
        if node == parent_lst[node]:
            return node 
        else:
            return self.get_parent(parent_lst[node])

    def check_parent(self, nodeA, nodeB):
        if self.get_parent(nodeA) == self.get_parent(nodeB):
            return True 
        else:
            return False 
    def union(self, nodeA, nodeB):
        if self.check_parent(nodeA, nodeB):
            return False 
        else:
            if self.get_parent(nodeA) < self.get_parent(nodeB):
                parent_lst[nodeB] = self.get_parent(nodeA)
            else:
                parent_lst[nodeA] = self.get_parent(nodeB)
            return True 
     
for i in range(M):
    start , end , dist = list(map(int, input().split(' ')))
    distance_lst.append(nodeinfo(start, end, dist))
    #distance_lst[i].union(start, end)
tag = 0 
total_dist = 0 
for f in sorted(distance_lst, key=lambda x: x.dist):
    print(f.dist)
    print(*parent_lst)
    if tag == 0:
        total_dist+= f.dist 
        f.union(f.a, f.b)
    else:
        if f.union(f.a, f.b) != False:
            total_dist += f.dist
    tag += 1
print(total_dist)
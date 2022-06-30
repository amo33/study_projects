from collections import deque
import sys 

lines = [
    [0,1,0,0,1,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0]
]

encounter_node = []

for i in range(7):
    cnt = 0
    for j in range(7):
        cnt += lines[j][i]
    encounter_node.append(cnt) 
nodes = deque()
for i in range(len(encounter_node)):
    if encounter_node[i] == 0:
        nodes.append(i)
print(nodes)

def topol(que):
    result_topology = []
    while que:
        val = que.popleft()
        result_topology.append(val+1)
        for i in range(7):
            if val != i:
                if lines[val][i] == 1:
                    encounter_node[i] -=1
                    if encounter_node[i] == 0:
                        que.append(i)
    if sum(encounter_node) != 0:
        return "cycle occur"
    return result_topology

print(topol(nodes))
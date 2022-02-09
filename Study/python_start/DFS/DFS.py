
def DFS(startnode,graph):
    need_visit , visited = [], []

    need_visit.append(startnode)

    while(need_visit):
        node = need_visit.pop() 
        if node not in visited: # list index = integer or slice 
            visited.append(node)
            need_visit.extend(graph[node])

    return visited   
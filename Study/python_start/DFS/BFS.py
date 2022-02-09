

def BFS(startnode, graph):
    need_visit, visited = [], []

    need_visit.append(startnode)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


def bfs(graph, node, goal):
    visited, queue=[], []
    visited.append(node), queue.append(node)

    while queue:
        m = queue.pop(0)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                if neighbour == goal:
                    return visited




graph = {
    '1': ['8', '5', '2'],
    '8': ['1','6', '4', '3'],
    '5': ['1'],
    '2': ['1', '9'],
    '6': ['8','10','7'],
    '4': ['8'],
    '3':['8'],
    '9':['2'],
    '10':['6'],
    '7':['6'],
}


print(bfs(graph,'1','7'))

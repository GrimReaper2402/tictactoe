graph = {
    '1': ['8', '5', '2'],
    '8': ['1', '6', '4', '3'],
    '5': ['1'],
    '2': ['1', '9'],
    '6': ['8', '10', '7'],
    '4': ['8'],
    '3': ['8'],
    '9': ['2'],
    '10': ['6'],
    '7': ['6'],
}
visited = []

def dfs(visited, graph, node, goal):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour == goal:
                visited.append(neighbour)
                #print("cost=", len(visited))
                print(visited)
                break
            dfs(visited, graph, neighbour, goal)

print("Depth-First Search")
initial = input("Enter initial node: ")
goal = input("Enter goal node: ")
dfs(visited, graph, initial, goal)
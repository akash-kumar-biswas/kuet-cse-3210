graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': [],
    'D': ['F','G'],
    'E': [],
    'F': ['H','I'],
    'G': ['J','K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


'''
def dfs(graph, start, vis):
    vis.add(start)

    print(start, end=" ")

    for child in graph[start]:
        if child not in vis:
            dfs(graph, child, vis)

vis = set()
dfs(graph, 'A', vis)
'''

def dfs(graph, start, target, vis, steps):
    vis.add(start)
    steps[0] += 1
    print(start, end=" ")

    if(start == target):
        return

    for child in graph[start]:
        if child not in vis:
            dfs(graph, child, target, vis, steps)

vis = set()
steps = [0]
dfs(graph, 'A', 'G', vis, steps)
print("\n", steps[0])

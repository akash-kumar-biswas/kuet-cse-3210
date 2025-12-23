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


def dls(graph, start, target, limit, vis):
    vis.add(start)
    print(start, end=" ")

    if(start == target):
        return True

    if(limit == 0):
        return False
    
    for child in graph[start]:
        if child not in vis:
            if dls(graph, child, target, limit - 1, vis):
                return True
    vis.remove(start)
    return False

def iddfs(graph, start, target, maxDepth):
    for depth in range(maxDepth + 1):
        print("\nDepth limit: ", depth)

        vis = set()

        if dls(graph, start, target, depth, vis):
            print("\nTarget found at depth:", depth)
            return True
    print("\nTarget not found")
    return False

start='A'
target='H'
maxDepth=4

print("\nTarget Found:", iddfs(graph, start, target, maxDepth))
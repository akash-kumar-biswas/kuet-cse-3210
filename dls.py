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

vis = set()
start = 'A'
target = 'G'
limit = 3

print("\nFound: ", dls(graph, start, target, limit, vis))
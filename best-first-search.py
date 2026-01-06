import heapq

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = []
    heapq.heappush(pq, (h(start, goal), start))  

    parent = {start: None}
    visited = set()      
    explored_count = 0

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        explored_count += 1

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            print(explored_count)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if neighbor not in visited:
                    heapq.heappush(pq, (h(neighbor, goal), neighbor))
                    parent[neighbor] = current

    return None

grid = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 0 (B at col 11)
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]   # row 6 (A at col 0)
]


start = (6, 0)   
goal = (0, 11)  
path = greedy_best_first(grid, start, goal)
print(path)
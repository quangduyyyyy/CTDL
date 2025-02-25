from collections import deque

def dfs(grid, start, goal):
    stack = deque()
    stack.append(start)
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()
        if current == goal:
            break
        if current in visited:
            continue
        visited.add(current)

        # Lấy các vị trí liền kề (trên, dưới, trái, phải)
        neighbors = get_neighbors(grid, current)

        # Kiểm tra xem đã tìm thấy đích chưa
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    return None
def get_neighbors(grid, position):
    neighbors = []
    x, y = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Trên, Dưới, Trái, Phải

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != 1:  # Nếu ô không phải là chướng ngại vật
                neighbors.append((nx, ny))
    
    return neighbors

if __name__ == "__main__":
    # Mình họa
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 3)
    path = dfs(grid, start, goal)
    print("Đường đi tìm được:", path)
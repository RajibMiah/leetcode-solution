def numIslands(grid):
    if not grid:
        return 0
    total_islands = 0
    for i, row in enumerate(grid):
        for j,  col in enumerate(row):
            if(grid[i][j] == '1'):
                bfs(grid, i, j)
                total_islands += 1
    return total_islands


def bfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '2'
    bfs(grid, i - 1, j)  # up
    bfs(grid, i + 1, j)  # down
    bfs(grid, i, j - 1)  # left
    bfs(grid, i, j + 1)  # right


print(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))  # output 1

print(numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # output 3

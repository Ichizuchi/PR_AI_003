def flood_fill(matrix, start_node, target_color, replacement_color):
    rows, cols = len(matrix), len(matrix[0])
    x, y = start_node
    if matrix[x][y] != target_color:
        return matrix

    def dfs(row, col):
        if not (0 <= row < rows and 0 <= col < cols):
            return
        if matrix[row][col] != target_color:
            return
        matrix[row][col] = replacement_color
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(row + dr, col + dc)

    dfs(x, y)
    return matrix

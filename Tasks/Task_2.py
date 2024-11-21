def longest_path_in_matrix(matrix, start_char):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    memo = {}

    def is_valid_move(x, y, prev_char):
        return 0 <= x < rows and 0 <= y < cols and ord(matrix[x][y]) == ord(prev_char) + 1

    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        max_path = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, matrix[x][y]):
                max_path = max(max_path, 1 + dfs(nx, ny))
        memo[(x, y)] = max_path
        return max_path

    max_length = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                max_length = max(max_length, dfs(i, j))
    return max_length

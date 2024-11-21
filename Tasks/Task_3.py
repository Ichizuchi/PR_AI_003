def find_words_in_matrix(board, dictionary):
    rows, cols = len(board), len(board[0])
    result = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_valid_move(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and (x, y) not in visited

    def dfs(x, y, path, visited):
        if path in dictionary:
            result.add(path)
        if len(path) > max(map(len, dictionary)):
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, visited):
                dfs(nx, ny, path + board[nx][ny], visited | {(nx, ny)})

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, board[i][j], {(i, j)})

    return result

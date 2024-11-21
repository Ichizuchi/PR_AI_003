# Функция для Flood fill 
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

# Функция для поиска самого длинного пути в матрице символов
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

# Функция для генерация списка возможных слов из матрицы символов 
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

def main():
    # Задание 1
    matrix = [
        ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
        ["Y", "Y", "Y", "G", "G", "G", "X", "X", "X", "X"],
        ["W", "W", "Y", "W", "G", "G", "G", "X", "X", "X"],
        ["W", "W", "W", "W", "G", "G", "G", "G", "G", "X"],
        ["W", "W", "W", "R", "R", "R", "R", "X", "X", "X"],
        ["W", "B", "R", "R", "R", "R", "R", "R", "R", "X"],
        ["W", "B", "B", "B", "B", "B", "B", "R", "X", "X"],
    ]
    start_node = (3, 9)
    target_color = "X"
    replacement_color = "C"
    
    print("Flood Fill Result:")
    result = flood_fill(matrix, start_node, target_color, replacement_color)
    for row in result:
        print(row)

    # Задание 2
    matrix = [
        ["D", "E", "H", "X", "B"],
        ["A", "O", "G", "P", "E"],
        ["D", "D", "C", "F", "D"],
        ["E", "B", "E", "A", "S"],
        ["C", "D", "Y", "E", "N"],
    ]
    start_char = "C"
    
    print("\nLongest Path Length:")
    print(longest_path_in_matrix(matrix, start_char))

    # Задание 3
    board = [
        ['М', 'С', 'Е'],
        ['Р', 'А', 'Т'],
        ['Л', 'О', 'Н']
    ]
    dictionary = {'МАРС', 'СОН', 'ТОН'}
    print("\nGenerated Words:")
    print(find_words_in_matrix(board, dictionary))

if __name__ == "__main__":
    main()

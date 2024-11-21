# Поиск в глубину по личному графу
from collections import deque

# Граф с расстояниями между городами
graph = {
    "Стамбул": [("Бурса", 155), ("Эскишехир", 480), ("Анкара", 450)],
    "Бурса": [("Стамбул", 155), ("Анкара", 480), ("Маниса", 70)],
    "Эскишехир": [("Стамбул", 480), ("Анкара", 230)],
    "Анкара": [("Эскишехир", 230), ("Стамбул", 450), ("Бурса", 480), ("Сивас", 320), ("Конья", 260)],
    "Маниса": [("Бурса", 70), ("Измир", 330)],
    "Измир": [("Маниса", 330), ("Анталья", 460)],
    "Конья": [("Анкара", 260), ("Анталья", 290), ("Мерсин", 460)],
    "Анталья": [("Измир", 460), ("Конья", 290)],
    "Мерсин": [("Конья", 460), ("Адана", 70)],
    "Адана": [("Мерсин", 70), ("Газантеп", 220)],
    "Газантеп": [("Адана", 220), ("Шанлыурфа", 150)],
    "Шанлыурфа": [("Газантеп", 150), ("Диярбакыр", 180)],
    "Диярбакыр": [("Шанлыурфа", 180), ("Ван", 320)],
    "Ван": [("Диярбакыр", 320), ("Эрзурум", 370)],
    "Эрзурум": [("Ван", 370), ("Трабзон", 250)],
    "Трабзон": [("Эрзурум", 250), ("Самсун", 330)],
    "Самсун": [("Трабзон", 330), ("Сивас", 410)],
    "Сивас": [("Самсун", 410), ("Анкара", 320), ("Кайсери", 240)],
    "Кайсери": [("Сивас", 240), ("Малатья", 240)],
    "Малатья": [("Кайсери", 240), ("Шанлыурфа", 90)]
}

def dfs_min_path(graph, start, goal, visited=None, path_cost=0):
    if visited is None:
        visited = set()
    if start == goal:
        return path_cost
    visited.add(start)
    min_cost = float('inf')
    for neighbor, cost in graph[start]:
        if neighbor not in visited:
            current_cost = dfs_min_path(graph, neighbor, goal, visited.copy(), path_cost + cost)
            min_cost = min(min_cost, current_cost)
    return min_cost

# Пример использования
start_city = "Стамбул"
goal_city = "Анкара"
min_distance = dfs_min_path(graph, start_city, goal_city)
print(f"Минимальное расстояние между {start_city} и {goal_city}: {min_distance}")

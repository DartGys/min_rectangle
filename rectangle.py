import itertools

def min_area_rectangle(points):
    if not points:
        return []

    # Знаходимо мінімальні та максимальні координати
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    # Повертаємо координати прямокутника
    return [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]

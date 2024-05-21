from scipy.spatial import ConvexHull

def min_area_rectangle(points):
    if not points:
        return []

    # Знаходимо опуклу оболонку для заданих точок
    hull = ConvexHull(points)

    # Знаходимо мінімальний прямокутник, охоплюючий опуклу оболонку
    hull_points = [points[i] for i in hull.vertices]
    min_x = min(hull_points, key=lambda p: p[0])[0]
    max_x = max(hull_points, key=lambda p: p[0])[0]
    min_y = min(hull_points, key=lambda p: p[1])[1]
    max_y = max(hull_points, key=lambda p: p[1])[1]

    # Повертаємо координати прямокутника
    return [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]

def point_in_polygon(point, polygon):
    """
    Determine if a point is inside a polygon using the Ray Casting Algorithm.
    :param point: A tuple (latitude, longitude).
    :param polygon: A list of tuples [(lat1, lng1), (lat2, lng2), ...].
    :return: True if the point is inside the polygon, False otherwise.
    """
    x, y = point
    n = len(polygon)
    inside = False

    p1 = polygon[0]
    for i in range(1, n + 1):
        p2 = polygon[i % n]
        if y > min(p1[1], p2[1]):
            if y <= max(p1[1], p2[1]):
                if x <= max(p1[0], p2[0]):
                    if p1[1] != p2[1]:
                        xinters = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
                    if p1[0] == p2[0] or x <= xinters:
                        inside = not inside
        p1 = p2

    return inside
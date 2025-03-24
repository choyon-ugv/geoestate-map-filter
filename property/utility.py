from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lng1, lat2, lng2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude to degrees to radians
    lat1, lng1, lat2, lng2 =  map (radians, [lat1, lng1, lat2, lng2])
    
    # Differences in coordinates
    dlat  = lat2 - lat1
    dlng = lng2 - lng1
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    # distance in kilometers
    distance = R * c
    return distance
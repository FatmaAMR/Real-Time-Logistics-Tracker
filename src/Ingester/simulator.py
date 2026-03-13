import time
import random

def move_truck(truck_id, current_pos, destination):
    step = 0.001 
    lat = current_pos['lat']
    lon = current_pos['lon']
    
    if lat < destination['lat']: lat += step
    else: lat -= step
    
    if lon < destination['lon']: lon += step
    else: lon -= step
    
    return {
        "truck_id": truck_id,
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "speed": random.randint(60, 120),
        "timestamp": time.time()
    }
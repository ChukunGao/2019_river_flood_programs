from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    
    """Requirements for Task 1B"""
    
    centre =  (52.2053, 0.1218)
    stations = build_station_list()

    distances = stations_by_distance(stations, centre)
    print(distances[:10])
    print(distances[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

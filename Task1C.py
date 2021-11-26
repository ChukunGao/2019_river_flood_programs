from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():

    """Requirements for Task 1C"""
    
    centre = (52.2053, 0.1218)
    radius = 10
    stations = build_station_list()

    enclosed = stations_within_radius(stations, centre, radius)
    printable = [x[0] for x in enclosed]
    print(printable)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

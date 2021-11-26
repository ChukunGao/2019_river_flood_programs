from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    temp = rivers_by_station_number(stations, 9)
    print(temp)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
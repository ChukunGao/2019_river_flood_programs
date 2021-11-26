from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_station
from floodsystem.geo import station_by_river

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    #get a list of stations and find length
    temp_1 = list(river_with_station(stations))
    print(len(temp_1))

    #print first 10 stations in alphabetical order
    temp_1.sort()
    for i in range(10):
        print(temp_1[i])

    #make a dictionary of all rivers to stations
    temp_2 = station_by_river(stations)
    print(sorted(temp_2['River Aire']), '\n', sorted(temp_2['River Cam']), '\n', sorted(temp_2['River Thames']))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
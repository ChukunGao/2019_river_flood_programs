from floodsystem.flood import stations_level_over_threshold as slot
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    ratios = slot(stations, 0.8)
    for i in ratios:
        print(i[:2])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

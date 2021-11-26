import datetime
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level as shrl
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt



def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    highest = shrl(stations, 5)

    for i in highest:
        # Station name to find
        station_name = i[0]

        dt = 10
        # Find station
        station_new = None
        for u in stations:
            if u.name == station_name:
                station_new = u
                break
        dates, levels = fetch_measure_levels(
            station_new.measure_id, dt=datetime.timedelta(days=dt))
        t = []
        waterlevel = []
        for date, level in zip(dates, levels):
            t.append(date)
            waterlevel.append(level)
        plot_water_levels(u, t, waterlevel)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
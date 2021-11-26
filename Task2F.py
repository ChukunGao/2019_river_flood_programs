import datetime
import matplotlib
import numpy as np
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level as shrl
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_levels_with_fit
def run():
    # Build list of stations
    stations = build_station_list(False)

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

        date_list = matplotlib.dates.date2num(dates)

        poly, d0 = polyfit(dates, levels, 4)
        date_list_shifted = []
        for i in range(len(date_list)):
            date_list_shifted.append(date_list[i] - d0)
        result = []

        for i in range(len(date_list_shifted)):
            result.append(poly(date_list_shifted[i]))
        plot_water_levels_with_fit(u, t, waterlevel, result)
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

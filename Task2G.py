from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.dates


"""For this system our category guidelines will correspond to the first four stages
of the US flood stage system:
https://en.wikipedia.org/wiki/Flood_stage#Flood_categories   """

def run(town):
    stations = build_station_list(False)
    update_water_levels(stations)
    low = []
    moderate = []
    high = []
    severe = []

    ratio_list = stations_level_over_threshold(stations, 1)

    for i in ratio_list:


        dt = 10
        for u in stations:
            if u.name == i[0]:
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



        for j in range(7):

            result = (poly(-j))

            typical_range = station_new.typical_range[1] - station_new.typical_range[0]
            offset = result - station_new.typical_range[0]
            ratio = offset / typical_range

            weighted_ratio = ratio/((j+1) ** 0.5)

            if weighted_ratio > 3 and i[2] not in severe:   
                severe.append(i[2])
            elif 2 < weighted_ratio <= 3 and i[2] not in severe and i[2] not in high:   
                high.append(i[2])
            elif 1.5 < weighted_ratio <= 2 and i[2] not in severe and i[2] not in high and i[2] not in moderate:  
                moderate.append(i[2])
            elif 1 <= weighted_ratio <= 1.5 and i[2] not in severe and i[2] not in high and i[2] not in moderate and i[2] not in low:  
                low.append(i[2])



        
        if i[1] > 3 and i[2] not in severe:   ## Levels are life-threatening, can cause catastrophic damage
            severe.append(i[2])
        elif 2 < i[1] <= 3 and i[2] not in severe and i[2] not in high:    ## Buildings starting to flood, some road closures
            high.append(i[2])
        elif 1.5 < i[1] <= 2 and i[2] not in severe and i[2] not in high and i[2] not in moderate:  ## Roads starting to flood but not buildings yet
            moderate.append(i[2])
        elif 1 <= i[1] <= 1.5 and i[2] not in severe and i[2] not in high and i[2] not in moderate and i[2] not in low:  ## River full, maybe slightly over banks
            low.append(i[2])




    
    

## Level 5, record flood, is not included as it is not necessarily helpful for a
## warning system - record level does not have to be even at low risk if the
## river has never flooded before

    if town != None:  ## Searches data for a specific town chosen by user
        if town in severe:
            print(town + " is at severe risk")
        elif town in high:
            print(town + " is at high risk")
        elif town in moderate:
            print(town + " is at moderate risk")
        elif town in low:
            print(town + " is at low risk")
        else:
            for i in range(len(stations)):
                station = stations[i]
                if station.town == town:
                    print(town + " is not at risk")
                    break
                elif i == len(stations) - 1 and station.town != town:
                    print("Data not available")
            
    else:  ## Outputs all data if user has not chosen a specific town
        print("Towns at low risk: ")
        print(low)
        print("Towns at moderate risk: ")
        print(moderate)
        print("Towns at high risk: ")
        print(high)
        print("Towns at severe risk: ")
        print(severe)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    q = input("Would you like to search for data on a specific town? (Y/N) ")
    if q in ("Y", "y", "Yes", "YES", "yes"):
        town = input("Which town would you like to check on? ")
    else:
        town = None
    run(town)

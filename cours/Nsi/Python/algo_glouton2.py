#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### Functions
#### Exercice ones
def isAvailableToDoParcours(full_distance: int, distance_stations: list) -> bool:
    """Function storing a condition and returning a bool value, can be called by others functions.

    Args
    ----

        `full_distance`: int
            A value of the distance we can reach with the fuel tank of the vehicle at full capacity.

        `distance_stations`: list
            A list containing the distance of the gas stations from each others.
    """
    max_dist = 0
    for i in range(0, len(distance_stations)): ### for-loop to check each distance.
        if distance_stations[i] > max_dist: ### Check if current value is greater than the value of max_dist
            max_dist = distance_stations[i] ### then define the current value as the value of the max_dist.
    if full_distance >= max_dist: ### Compare if the biggest distance we can reach is greater or equal to the maximum distance we'll have.
        return True ### if true return True
    return False ### otherwise return False

def doSmallestStops(fuel_distance: int, distance_stations: list) -> list:
    """Function to find the smallest stops done while doing the parcours.

    Args
    ----

        `fuel_distance`: int
            A value used to determine the distance which can be done with a full fuel tank of the vehicle.

        `distance_stations`: list
            A list containing the distance of the gas stations from each others.
    """
    if isAvailableToDoParcours(fuel_distance, distance_stations) is True: ### Using the condition function to check whether the driver can do or not the parcours
        initial_fuel = fuel_distance ### We save the inital amount, we'll be using it for marking a stop at a gas station.
        stations_to_stop = [] ### define the list we'll be returning with the gas stations we've stopped in it.
        fuel_distance -= distance_stations[0]
        for i in range(0, len(distance_stations)-1): ### len(distance_stations)-1 to not have a IndexError due to a out of range index. 
            if (fuel_distance-distance_stations[i+1]) >= 0: ### If we have more gas or the amount needed to reach the next station
                fuel_distance -= distance_stations[i+1] ### then substract the fuel we'll be consumming for reaching it.
            else: ### Otherwise we stop at this station and put again fuel at full capacity
                stations_to_stop.append(i) ### and we append the station in our needed-stop-by-stations list
                fuel_distance = initial_fuel
                fuel_distance -= distance_stations[i+1] ### then substract the fuel we'll be consumming for reaching it.
        return stations_to_stop ### Return the list of the stations we'll need to stop by.
    else:
        raise Exception("This driver can't do the parcours") ### Raise an exception if the driver can't do the parcours.

def chooseSeance(criteria: str, seance_list: list, criteria_value=60, multiple_seances=True, difference=20, index_seance_needed=None) -> str:
    """Function to choose a certain amount of seances in a planning.

    Args
    ----

        `criteria`: str
            One of the three options `start_time`, `length`, `end_time`.

        `seance_list`: list
            A list containing the data needed to for each criteria.

        `criteria_value`: int, optional
            A value substracted by the value of elements already picked by criteria used to offer the best choice.

        `multiple_seances`: bool, optional
            A bool used to know if we want one seance or many.

        `difference`: int, optional
            A value used to pick the closest seances of the criteria_value in a certain proportion.

        `index_seance_needed`: int, optional
            The index of the seance we want to assist at all cost, by default defined as None.
    """
    l = list()
    if criteria == "start_time": search_key = "debut" ### keyword used in the dict storing the database
    elif criteria == "length": search_key = "duree" ### //
    elif criteria == "end_time": search_key = "fin" ### //
    else: ### returning an exception with an error message because of a wrong criteria given, so not supported.
        raise Exception("This function does not support any other criteria.\n Try again using one of the supported ones.")
    for seance_index in seance_list:
        l.append([abs(criteria_value-seance_list[seance_index][search_key]), seance_list[seance_index][search_key], seance_index, False]) ### creating dict to store: the abs value of the difference of the criteria given, value of elem, index of elem, boolean value used to know if put in the returned str.
        current_index = l.index([abs(criteria_value-seance_list[seance_index][search_key]), seance_list[seance_index][search_key], seance_index, False]) ### Picking the index of the newly created element of l, it will save us a lot of time of code-writing.
        if index_seance_needed is not None: ### If want to participate to a seance in particular, then turn the search into a specialized one.
            if l[current_index][2] == index_seance_needed: ### If it's the seance wanted
                l[current_index][3] = True ### then add it in our returned str
            else:
                if True: 
                    if l[current_index][0] <= difference: ### If under our difference, toggle the bool value to add it in our return str
                        l[current_index][3] = True
                    else:
                        l[current_index][3] = False
                else:
                    l[current_index][3] = False
        else: ### If index_seance_needed is None we use a simplest method to know which seance we need to return
            if l[current_index][0] <= difference:
                l[current_index][3] = True
            else:
                l[current_index][3] = False
    l.sort()
    ### An if-else condition used to avoid a too big processing request while it's only needed to have a little one.
    ### If condition is true, user asked for only one seance so we only add the first data set in our list.
    ### Otherwise we use a for-loop to add each data set in the returning str.
    ###
    ### Two external functions called are: `renderHour()` and `minsToHrs()`
    ### They are used to ease the output reading.
    ### Check the comments written before the creation of the database to understand.
    if multiple_seances is False:
        r = f"With the criteria: \"{criteria}\", the result is:\n"
        r += f"\t- {l[0][2]}: debut = {renderHour(minsToHrs(seance_list[l[0][2]]['debut']))}, fin = {renderHour(minsToHrs(seance_list[l[0][2]]['fin']))}, duree = {seance_list[l[0][2]]['duree']}\n"
    else:
        r = f"With the criteria: \"{criteria}\", the results are:\n"
        for seance_data in l:
            if seance_data[3] is True:
                r += f"\t- {seance_data[2]}: debut = {renderHour(minsToHrs(seance_list[seance_data[2]]['debut']))}, fin = {renderHour(minsToHrs(seance_list[seance_data[2]]['fin']))}, duree = {seance_list[seance_data[2]]['duree']}\n"
    return r

#### Utils | Do not mind it, used to simplify the calculations and the work btw
def minsToHrs(minutes: int):
    """Function used to transform minutes in hours.

    Args
    ----

        `minutes`: int
            The amount of minutes we have.
    
    Input exemple:
    --------------

        `1h30` will be passed as `90` then processed, 1.3 will be returned.
    """
    full_hour = False
    full_hours = minutes//60 ### Calculate the full hours
    mins = minutes%60 ### calculate the minutes left
    r = float(full_hours+(mins/100)) ### mins/100 = transforming the amount of minutes into a floating number in order to respect the format used by the functions
    if int(r) == r: ### if final result is a full hour then toggle the variable to True
        full_hour = True
    if full_hour is True: ### If full_hour is True then return an int() object of the hour
        return int(r) ### used to pass through a bug which creates a final abnormal writing of a full hour, transforming output from 1h0 to 1h
    return r ### Otherwise return the float() object

def hrsToMins(hours: float) -> int:
    """Function used to transform hours in minutes. Returns an int().

    Args
    ----

        `minutes`: float 
            the format used is as it were written, we just replace the 'h' in the writing by a dot.

    Input exemple:
    --------------

        `1h30` is passed as `1.3` then processed, 90 will be returned.
    """
    full_hours = int(hours)*60 # calculate the precedent hour without the minutes
    mins = int((hours-int(hours))*100) #If it's not a full hour, transform the minutes left into the result, passing from float() to int() by multiplying it by 100
    return full_hours+mins

def renderHour(hour):
    """Function to format the string of the hour, increasing the readibility of the ouput.

    Args
    ----

        `hour`: int or float
            An hour which will be formatted in order to ease the readibility.
    """
    if type(hour) is int:
        return f"{hour}h" ### If hour is an int() we just add the 'h' to it (and transfroms it in a str() btw)
    else:
        return f"{hour}".replace(".", "h") ### Otherwise we replace the dot of the float() by the 'h' for the hour (and transfroms it in a str() too)

### Global vars
#### Exercice 1
d_base = [23, 40, 12, 44, 21, 9, 67, 32, 51, 30, 11, 55, 24, 64, 32, 57, 12, 80]
r_base = 100
#### Exercice 2

### The database of the seances is defined in an uncommon way, it's defined using a call to the dict() class cosntructor for the data set in each seance.
### For a simplicity of calculating, we use a function called `hrsToMin()` to transform the hours written in the exercise into minutes
### It's more convenient for calculs, but in order to not lose the reader of the outputs of the script we will call later, two functions. 
### The first one is the opposite of the function called at start, she'll transform the minutes into hours in the same format used below.
### The second one is used to ease the reading and comprehension of the reader, it will adjust the ouput of the hours in order to have anyone able to read to understand what's written.
### For a more little more profound understanding of how it works, check out either the docstring of the functions using `help()` or looking at the code in each functions, the are surely commented btw.
seances = {
    1: dict(debut=hrsToMins(9), fin=hrsToMins(11), duree=120),
    2: dict(debut=hrsToMins(9.15), fin=hrsToMins(10.5), duree=95),
    3: dict(debut=hrsToMins(10), fin=hrsToMins(11.20), duree=80),
    4: dict(debut=hrsToMins(13), fin=hrsToMins(15.25), duree=145),
    5: dict(debut=hrsToMins(15), fin=hrsToMins(16.40), duree=100),
    6: dict(debut=hrsToMins(15.15), fin=hrsToMins(18.15), duree=180),
    7: dict(debut=hrsToMins(16), fin=hrsToMins(18.05), duree=125),
    8: dict(debut=hrsToMins(17.30), fin=hrsToMins(19), duree=90),
    9: dict(debut=hrsToMins(18), fin=hrsToMins(20.1), duree=130),
    10: dict(debut=hrsToMins(19.30), fin=hrsToMins(22), duree=150),
}


### Execution Bloc
print(f"Ex1: Question 9.5.1:\n\t{isAvailableToDoParcours(r_base, d_base)}", end="\n\n")
print(f"Ex1: Question 9.5.2:\n\t{doSmallestStops(r_base, d_base)}", end="\n\n")
print("Ex2: Question b:\n\t-`critère A`: Aucun trouvé")
print("\t-`critère B`: Aucun trouvé")
print("\t-`critère C`: Aucun trouvé")
print(f"Ex2: Question c:\n{chooseSeance('length', seances, 80, difference=20)}\n{chooseSeance('start_time', seances, hrsToMins(14), difference=200)}\n{chooseSeance('end_time', seances, hrsToMins(16), difference=200)}", end="\n\n")
print(f"Ex2: Question d:\n{chooseSeance('length', seances, 80, difference=20, index_seance_needed=9)}\n{chooseSeance('start_time', seances, hrsToMins(14), difference=200, index_seance_needed=9)}\n{chooseSeance('end_time', seances, hrsToMins(16), difference=200, index_seance_needed=9)} ")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### Functions
def ParcoursRoad(arg1, arg2):
    status = 0
    for gas_station in arg2:
        status += gas_station
        if arg2.index(gas_station)+1 < len(arg2):
            print(f"Status: {status}, {status+arg2[arg2.index(gas_station)+1]}; {arg2.index(gas_station)}, {arg2.index(gas_station)+1}")
        else:
            print(f"Status: {status}, {arg2.index(gas_station)}")

### Global vars
d_base = [23, 40, 12, 44, 21, 9, 67, 32, 51, 30, 11, 55, 24, 64, 32, 57, 12, 80]
r_base = 100

### Execution Bloc
print("Question 9.5.1:\n\ttest")
ParcoursRoad(r_base, d_base)

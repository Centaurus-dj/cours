import sys
import os
from os import environ
environ["PWD"] = "home/alexis/Documents/cours/cours/Nsi/algo_knn"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Imports
import pandas as pds
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


### Functions
def templateFunction(data: DataFrame, save=True, filename="pic"):
    x = data.loc[:,"petal_length"]
    y = data.loc[:,"petal_width"]
    lab = data.loc[:,"species"]

    fig = plt.figure()
    plt.axis('equal')
    plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
    plt.scatter(x[lab == 1], y[lab == 1], color='r', label='versicolor')
    plt.scatter(x[lab == 2], y[lab == 2], color='b', label='virginica')
    plt.legend()
    if save is True:
        fig.savefig(f"{filename}.png")
    else:
        plt.show()



### Global variables
iris = pds.read_csv(os.path.realpath("cours/Nsi/algo_knn/iris.csv"))

### Execution column
templateFunction(iris, False, "iris_data")
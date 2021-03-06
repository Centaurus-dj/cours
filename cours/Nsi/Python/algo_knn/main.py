#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from os import environ

from numpy import sqrt
from modules.csv_reader import csvReader
environ["PWD"] = "home/alexis/Documents/cours/cours/Nsi/algo_knn"


### Imports
import pandas as pds
from matplotlib import (
    pyplot as plt,
)
from pandas.core.frame import DataFrame
from sklearn.neighbors import KNeighborsClassifier


### Functions
def templateFunction(data: DataFrame, save=True, filename="pic", filepath=""):
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
        if sys.version[8] == "3":
            exec("""fig.savefig(f"{filepath}{filename}.png")""")
        else:
            print("WARNING: You have an old version of Python, be sure to update it as soon as possible")
            fig.savefig("{}{}.png".format(filepath, filename))
    else:
        plt.show()

def templateFunction2(data: DataFrame, save=True, filename="pic", filepath="", length=2.5, width=0.75, k_base=3, fontsize=12, return_kind=False, kinds_lib=None):
    x = data.loc[:,"petal_length"]
    y = data.loc[:,"petal_width"]
    lab = data.loc[:,"species"]
    print(lab)

    ### valeurs
    longueur = length
    largeur = width
    k = k_base

    ### graphique
    fig = plt.figure()
    plt.axis('equal')
    plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
    plt.scatter(x[lab == 1], y[lab == 1], color='r', label='versicolor')
    plt.scatter(x[lab == 2], y[lab == 2], color='b', label='virginica')
    plt.scatter(longueur, largeur, color='k')
    plt.legend()

    #algo knn
    d = list(zip(x,y))
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(d,lab)
    prediction = model.predict([[longueur,largeur]])

    ### Library of kinds of data
    if kinds_lib is None:
        kinds_lib = {
            "iris": ["setosa", "versicolor", "virginica"]
        }

    #Affichage resultats
    returned = ""
    txt = "Résultat : "
    
    if prediction[0] == 0:
        returned = kinds_lib["iris"][0]
    if prediction[0] == 1:
        returned = kinds_lib["iris"][1]
    if prediction[0] == 2:
        returned = kinds_lib["iris"][2]
    txt += returned

    if return_kind is True:
        return returned

    if sys.version[8] == "3":
        plt.text(3,0.5, f"largeur : {largeur} cm longueur : {longueur} cm", fontsize=fontsize)
        plt.text(3,0.3, f"k : {k}", fontsize=fontsize)
        plt.text(3,0.1, txt, fontsize=fontsize)
        if save is True:
            fig.savefig("{fielpath}{filename}.png")
        else:
            plt.show()

def CustomFunction(dataset: list, save=True, filename="graph", 
    filepath="", length=2.5, width=0.75, 
    k_base=3, fontsize=12, return_kind=False, kinds_lib=None):
    """A function using KNN algorithm, a machine learning algorithm. | Semi-dynamic function

    Args
    ----
        `dataset`: list
            The set of data passed to the function. 
            --> Dynamic use

        `save`: bool, optional
            `True`: We save the graph returned in a PNG file.
            `False`: We show the graph in a GUI with matplotlib module.
            --> Dynamic use

        `filename`: str, optional
            The name of the file we'll save, by default it's "graph".
            --> Dynamic use

        `filepath`: str, optional
            The path for storing the file.
            --> Dynamic use

        `length`: float, int, optional
            The length of the iris.
            --> Semi-dynamic use

        `width`: float, int, optional
            The width of the iris.
            --> Semi-dynamic use

        `k_base`: float, int, optional
            The k value we'll use by default.
            --> Semi-dynamic use

        `fontsize`: float, int, optional
            The size of the font of the text in the graph.
            --> Dynamic use

        `return_kind`: bool, optional
            `True`: We return the found kind of iris before the creation of a graph.
            `False`: We create a graph returning the kind and the data searched.
            --> Dynamic use.

        `kinds_lib`: dict, optional
            A dictionary storing the different kinds of iris.
            --> Static use
    """
    def square(to_square):
        return to_square**2

    def classifyNeighbors(d1, d2, label):
        neighbor_prox = list()
        neighbor_prox.append([sqrt(square(d2[0]-d1[0])+square(d2[1]-d1[1])), label])
        return neighbor_prox
    
    def kAlgo(base, data, label):
        r = list()
        for dataset in data:
            r.append(classifyNeighbors(base, dataset, label[data.index(dataset)]))
        return r
    
    def predict(dataset, test_number=5):
        def mostFrequent(list):
            d = dict()
            most_value = []
            for elem in list:
                if elem[0][1] not in d.keys():
                    d[elem[0][1]] = 0
                d[elem[0][1]] += 1
            for key, value in d.items():
                if most_value == []:
                    most_value = [value, key]
                if value > most_value[0]:
                    most_value = [value, key]
            return most_value[1]

        dataset.sort()
        l = list()
        x = 0
        for data in dataset:
            if x <= (test_number-1):
                l.append(data)
                x += 1
            else:
                break
        return (l, mostFrequent(l))

    dataset.pop(0)
    data = dict(x=[], y=[], lab=[], y_sorted=dict(), x_sorted=dict())
    for curr_data in dataset:
        data["x"].append(float(curr_data[0]))
        data["y"].append(float(curr_data[1]))
        data["lab"].append(curr_data[2])

    ### valeurs
    longueur = length
    largeur = width
    k = k_base
    
    for lab_i in range(0, 3):
        data["x_sorted"][f"lab=={lab_i}"] = [data["x"][i] for i in range(0, len(data["lab"])) if [lab == str(lab_i) for lab in data["lab"]][i]]
        data["y_sorted"][f"lab=={lab_i}"] = [data["y"][i] for i in range(0, len(data["lab"])) if [lab == str(lab_i) for lab in data["lab"]][i]]


    ### graphique
    fig = plt.figure()
    plt.axis('equal')   
    plt.scatter(data["x_sorted"]["lab==0"], data["y_sorted"]["lab==0"], color='g', label='setosa')
    plt.scatter(data["x_sorted"]["lab==1"], data["y_sorted"]["lab==1"], color='r', label='versicolor')
    plt.scatter(data["x_sorted"]["lab==2"], data["y_sorted"]["lab==2"], color='b', label='virginica')
    plt.scatter(longueur, largeur, color='k')
    plt.legend()

    #algo knn
    d = list(zip(data["x"], data["y"]))
    model = kAlgo((longueur, largeur), d, data["lab"])
    prediction = predict(model, k)
    
    ### Library of kinds of data
    if kinds_lib is None:
        kinds_lib = {
            "iris": ["setosa", "versicolor", "virginica"]
        }

    #Affichage resultats
    returned = ""
    txt = "Résultat : "
    
    if prediction[1] == str(0):
        returned = kinds_lib["iris"][0]
    if prediction[1] == str(1):
        returned = kinds_lib["iris"][1]
    if prediction[1] == str(2):
        returned = kinds_lib["iris"][2]
    txt += returned

    if return_kind is True:
        return returned
    print(prediction[0])
    rayon=prediction[0][k-1][0]

    plt.text(3,0.5, f"largeur : {largeur} cm longueur : {longueur} cm", fontsize=fontsize)
    plt.text(3,0.3, f"k : {k}", fontsize=fontsize)
    plt.text(3,0.1, txt, fontsize=fontsize)

    circle = plt.Circle((longueur, largeur), radius=rayon[0], color="g", fill=False)
    ax = plt.gca()
    ax.add_patch(circle)
    plt.axis("scaled")

    if save is True:
        fig.savefig(f"{filepath}{filename}.png")
    else:
        plt.show()


### Objects
if __name__ == "__main__":
    cr = csvReader("iris.csv", ",")

    CustomFunction(cr.get(), True, "graph_cricle")

if __name__ != "__main__":
    ### Global variables \\ Two variants to toggle for which way used to launch script
    iris = pds.read_csv(os.path.realpath("iris.csv")) ### Shell variant
    #iris = pds.read_csv(os.path.realpath("cours/Nsi/algo_knn/iris.csv")) ### VS Code variant


    ### Execution column
    templateFunction(iris, True, "iris_data")
    templateFunction2(iris, True, "iris_data2")
    templateFunction2(iris, True, "iris_data3_k=5", k_base=5)
    print("Si k=5, l'iris est:", templateFunction2(iris, k_base=5, return_kind=True))
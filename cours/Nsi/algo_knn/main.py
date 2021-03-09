#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from os import environ
from modules.csv_reader import csvReader
environ["PWD"] = "home/alexis/Documents/cours/cours/Nsi/algo_knn"


### Imports
import pandas as pds
import matplotlib.pyplot as plt
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
    print("x:", x, end="\n\n")
    y = data.loc[:,"petal_width"]
    print("y:", y, end="\n\n")
    lab = data.loc[:,"species"]
    print("lab:", lab, end="\n\n")

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

def CustomFunction(data: list, save=True, filename="pic", filepath="", length=2.5, width=0.75, k_base=3, fontsize=12, return_kind=False, kinds_lib=None):
    head = data.pop(0)
    x = list()
    y = list() 
    lab = list()
    for elem in data:
        x.append((float(elem[head.index(head[0])]), elem[head.index(head[2])]))
        y.append((float(elem[head.index(head[1])]), elem[head.index(head[2])]))
        lab.append(elem[head.index(head[2])])

    ### valeurs
    longueur = length
    largeur = width
    k = k_base

    ### graphique
    fig = plt.figure()
    plt.axis('equal')
    plt.scatter(x[0] if x[1 == 0]else pass, y[1 == 0], color='g', label='setosa')
    plt.scatter(x[1 == 1], y[1 == 1], color='r', label='versicolor')
    plt.scatter(x[1 == 2], y[1 == 2], color='b', label='virginica')
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
### Objects
if __name__ == "__main__":
    cr = csvReader("iris.csv", ",")

    CustomFunction(cr.get(), False)

if __name__ != "__main__":
    ### Global variables \\ Two variants to toggle for which way used to launch script
    iris = pds.read_csv(os.path.realpath("iris.csv")) ### Shell variant
    #iris = pds.read_csv(os.path.realpath("cours/Nsi/algo_knn/iris.csv")) ### VS Code variant


    ### Execution column
    templateFunction(iris, True, "iris_data")
    templateFunction2(iris, True, "iris_data2")
    templateFunction2(iris, True, "iris_data3_k=5", k_base=5)
    print("Si k=5, l'iris est:", templateFunction2(iris, k_base=5, return_kind=True))
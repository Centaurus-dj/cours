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
        fig.savefig(f"{filepath}{filename}.png")
    else:
        plt.show()

def templateFunction2(data: DataFrame, show=True, filename="pic", filepath=""):
    x = data.loc[:,"petal_length"]
    y = data.loc[:,"petal_width"]
    lab = data.loc[:,"species"]

    ### valeurs
    longueur=2.5
    largeur=0.75
    k=3

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

    #Affichage résultats
    txt = "Résultat : "
    
    if prediction[0] == 0:
        txt += "setosa"
    if prediction[0] == 1:
        txt += "versicolor"
    if prediction[0] == 2:
        txt += "virginica"

    plt.text(3,0.5, f"largeur : {largeur} cm longueur : {longueur} cm", fontsize=12)
    plt.text(3,0.3, f"k : {k}", fontsize=12)
    plt.text(3,0.1, txt, fontsize=12)
    
    if show is True:
        plt.show()
    else:
        fig.savefig(f"{filepath}{filename}.png")



### Global variables \\ Two variants to toggle for which way used to launch script
iris = pds.read_csv(os.path.realpath("iris.csv")) ### Shell variant
#iris = pds.read_csv(os.path.realpath("cours/Nsi/algo_knn/iris.csv")) ### VS Code variant


### Execution column
templateFunction(iris, False, "iris_data")
templateFunction2(iris, False, "iris_data2")
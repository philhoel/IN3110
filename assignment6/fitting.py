import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics
import data
import scipy as sp

def fit(training, validation, input_array, algorithm='knn', n=1, printing=True):

    """
    Uses K-Nearest-Neighbor or SVC algorithm to train on data set
    returns classifier and score of accuracy

    Parameters:
        training - training set
        validation - validation set
        input_array - which set to be on x and y axis
        algorithm - Which algorithm to use. KNN or SVC
        n - number for KNN
        printing - whether to print or not
    """
    if algorithm == 'knn':
        clf = KNeighborsClassifier(n_neighbors=n)
    elif algorithm == 'SVC':
        clf = SVC(gamma='scale')

    if all(isinstance(i, int) for i in input_array):
        datapoints = training.iloc[:, [i for i in input_array]]
        v_data = validation.iloc[:, [i for i in input_array]]
    elif all(isinstance(i, type('string')) for i in input_array):
        datapoints = training[[i for i in input_array]]
        v_data = validation[[i for i in input_array]]
    else:
        print('input_array must contain type "int" or type "string"')
        raise TypeError

    
    target = np.ravel(training[['diabetes']].replace('neg', 0).replace('pos', 1))
    v_target = np.ravel(validation[['diabetes']].replace('neg', 0).replace('pos', 1))
    clf.fit(datapoints, target)

    predicting = clf.predict(v_data)
    score = metrics.accuracy_score(v_target, predicting)
    if printing == True:
        print(metrics.accuracy_score(v_target, predicting))
    return clf, score

    


if __name__ == "__main__":

    arr = [4, 3]
    df_t, df_v = data.setup('diabetes.csv', 0.8)
    clf, score = fit(df_t, df_v, arr, 'knn', n=1)
    plot_iris(clf)
    
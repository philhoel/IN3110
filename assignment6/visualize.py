import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import sklearn
import data
import fitting
from sklearn import metrics


def visualization(file, array):

    """
    Creates a meshgrid and calles plot function from data.py

    Parameters:
        file - file to be used, must be .csv
        array - array of x and y axis
    """

    if len(array) < 2 or len(array) > 2:
        print("Array must be 2 elements to visualize")
        raise ValueError

    training, validation = data.setup(file)

    print(f'The accuracy of training for {array[0]} and {array[1]} is:')
    clf, score = fitting.fit(training, validation, array)

    x_min, x_max = np.array(validation[array[0]]).min() - 1, np.array(validation[array[0]]).max() + 1
    y_min, y_max = np.array(validation[array[1]]).min() - 1, np.array(validation[array[1]]).max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2), np.arange(y_min, y_max, 0.2))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, alpha=0.5, cmap='coolwarm')
    data.plot(validation, array=array)
    

    return score




if __name__ == "__main__":

    visualization('diabetes.csv', ['pregnant', 'age'])
    plt.show()



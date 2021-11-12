import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sys
import argparse


def setup(file, t_value=0.8):

    """
    Takes in a csv file. Name must be string.
    Also takes in how many procentage the training and validation set should
    be divided at. Defaults to 80% to training set and 20% validation set
    Must be given in as a float under 1

    Parameters:
        file - the file to use
        t_values - percentage to give as training set
    """

    if isinstance(file, type('string')):
        df = pd.read_csv(file)
        df = df.dropna()
        df = df.set_index(df.columns[0])
    else:
        print(f"Filename must be string, not {type(file)}")
        raise TypeError

    df_pos = df[df["diabetes"] == 'pos']
    df_neg = df[df["diabetes"] == 'neg']

    training_set = pd.merge(df_pos.iloc[int(len(df_pos)*(1-t_value)):, :], df_neg.iloc[int(len(df_pos)*(1-t_value)):, :], how='outer')
    validation_set = pd.merge(df_pos.iloc[:int(len(df_pos)*(1-t_value)), :], df_neg.iloc[:int(len(df_pos)*(1-t_value)), :], how='outer')
    
    return training_set, validation_set

def plot(data, x=None, y=None, array=None):

    """
    Creates a color list to plot either red or blue
    Plots then a scatter plot of all the values

    Parameters:
        data - The pandas.DataFrame object
        x - x-axis
        y - y-axis
        array - x and y given in as one array
    """
    color = []
    for i in data.iloc[:,-1]:
        if i == 'pos' or i == 1:
            color.append('red')
        else:
            color.append('blue')

    if x == None and y == None:
        if len(array) < 2 or len(array) > 2:
            print("Array must be only 2 inputs to plot")
            sys.exit()
        
        if all(isinstance(i, int) for i in array):
            plt.grid()
            plt.scatter(data.iloc[:,array[0]], data.iloc[:, array[1]], c=color)
            plt.xlabel(array[0])
            plt.ylabel(array[1])
            #plt.show()
        elif all(isinstance(i, type('string')) for i in array):
            plt.grid()
            plt.scatter(data[array[0]], data[array[1]], c=color)
            plt.xlabel(array[0])
            plt.ylabel(array[1])
            #plt.show()
        else:
            print("Must be all string or all int")
            raise TypeError
    else:
        plt.grid()
        plt.scatter(data[x], data[y], c=color)
        plt.xlabel(x)
        plt.ylabel(y)
        #plt.show()



if __name__ == "__main__":

    df_t, df_v = setup('diabetes.csv', 0.8)
    plot(df_t, 'insulin', 'mass')

    df_t, df_v = setup('diabetes.csv')
    new_list = [i for i in df_t]
    print(new_list)


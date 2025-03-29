'''
Author: Hunter Van Horn
Date: 02/27/2025
This program graphs the data collected while measuring circuit from lab7
'''
import numpy as np
import matplotlib.pyplot as plt

def experimentPlot():
    readFile = open('results.txt', 'r')
    values = readFile.readlines()
    readFile.close()

    temp = []

    for iter in values:
        temp.append(iter.replace(' ','').replace('\n','').split('|'))

    allValues = np.array(temp, dtype='d')
    frequency = allValues[:,1]*1000
    current = (allValues[:,2]/1000)
    impedance = 2/current
    angle = allValues[:,3]

    print(frequency)
    print(current)
    print(impedance)
    print(angle)

    plt.plot(frequency, impedance)
    plt.semilogx()
    plt.show()
    plt.plot(frequency, angle)
    plt.semilogx()
    plt.show()

if __name__ == "__main__":
    experimentPlot()
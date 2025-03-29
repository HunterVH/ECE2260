'''
Author(s): Hunter Van Horn, Dexter Ward
Date: 02/20/2025
This program will graph a series RLC circuit with variable resistance values
'''

import numpy as np
import matplotlib.pyplot as plt

'''
r - float, value of the resistor
c - float, value of the capacitor
l - float, value of the inductor
vco - float, initial voltage across the capacitor
vcf - float, final voltage across the capacitor
ico - float, initial current through the capacitor
t - array, values of time to measure the RLC circuit across
'''
def seriesRLC(r, c, l, vco, vcf, ico, t):
    p1 = 1
    p2 = r/l
    p3 = 1/(c*l)
    s1, s2 = np.roots([p1,p2,p3])

    if(s1.imag):
        matrix = np.array([[1,0],[s1.real, s1.imag]])
        answers = np.array([vco-vcf, ico/c])

        a, b = np.linalg.solve(matrix,answers)
        return a*np.exp(s1.real*t)*np.cos(s1.imag*t)+b*np.exp(s1.real*t)*np.sin(s1.imag*t)+vcf
    elif(s1 != s2):
        matrix = np.array([[1,1],[s1, s2]])
        answers = np.array([vco-vcf, ico/c])

        a, b = np.linalg.solve(matrix,answers)
        return a*np.exp(s1*t)+b*np.exp(s2*t)+vcf
    else:
        matrix = np.array([[1,0],[s1,1]])
        answers = np.array([vco-vcf, ico/c])

        a, b = np.linalg.solve(matrix,answers)
        return a*np.exp(s1*t)+b*np.exp(s2*t)*t+vcf

    

if __name__ == "__main__":
    c = .01E-6
    l = 1E-3
    r = [100, 200, 300, 400, 500, (2*np.sqrt(l/c)), 700, 800, 850, 900, 1000]
    vco = 0
    vcf = 5
    ico = 0
    t = np.arange(0, .0001, .00000001)
    
    for iter in r:
        voltages = seriesRLC(iter, c, l, vco, vcf, ico, t)
        plt.plot(t,voltages, label=f'{iter:.3f}')

    plt.legend(title='resistance', loc='lower right')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()
    
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

'''
num - The coefficients in the numerator
den - The coefficients in the denominator
time - The time value to calculate the final solution

Returns: 
np.real(answers) - The real portion of the calculated point

This function calculates the inverse laplace of a given equation, at a specified
time value, by using the numerator's and denominator's coefficients
'''
def inverse_laplace(num, den, time):
    def partialInverse(const, root, time, inst=1):
        if inst == 1:
            return const*np.exp(root*time)
        else:
            return (const/sci.special.factorial(inst-1))*np.exp(root*time)*time**(inst-1)
        
    instance = 1
    trackRoot = None
    answers = np.zeros((len(time)), dtype='complex128')
    
    r, p, k = sci.signal.residue(num, den)

    for iter in range(len(p)):
        if trackRoot == p[iter]:
            instance += 1
        else:
            instance = 1
            trackRoot = p[iter]

        answers += partialInverse(r[iter], p[iter], time, instance)

    if(np.argwhere(np.imag(answers)>1E-10).size):
        print('ERROR: AN IMAGINARY VALUE MADE IT TO THE THE FINAL SOLUTION')
    
    return np.real(answers)

'''
numCoeff - The coefficients of the numerator
denCoeff - The coefficients of the denominator
analySolution - The function that returns the analytical solution for the inverse laplace equation
time - A range of values to calculate the inverse laplace equation across

This function plots the analytical solution and the inverse laplace function solution
of the given equation across a range of times to compare the graphs
'''
def compareInverse(numCoeff, denCoeff, analySolution, time):
    plt.plot(time, inverse_laplace(numCoeff,denCoeff, time), '+', label='inverse')
    plt.plot(time, analySolution(time), label='analytical')
    plt.legend()
    plt.show()

'''
This function defines the analytical solutions to the inverse laplace equations
and makes the function calls to produce comparison graphs
'''
def main():
    def analyRealDist(t):
        return 120-72*np.exp(-8*t)+48*np.exp(-6*t)
    
    def analyComplexDist(t):
        return -24*t*np.exp(-3*t)*np.cos(4*t)+6*np.exp(-3*t)*np.cos(4*t-(np.pi/2))
    
    def analyRealRep(t):
        return 20-200*t**2*np.exp(-5*t)-100*t*np.exp(-5*t)-20*np.exp(-5*t)
    
    def analyComplexRep(t):
        return -12*np.exp(-6*t)+np.exp(-3*t)*(12*np.cos(4*t)+16*np.sin(4*t))
    
    time = np.arange(0,5,.01)

    compareInverse([96, 1632, 5760], [1, 14, 48, 0], analyRealDist, time)
    compareInverse([768], [1, 12, 86, 300, 625], analyComplexDist, time)
    compareInverse([100,2500], [1, 15, 75, 125, 0], analyRealRep, time)
    compareInverse([100,300], [1, 12, 61, 150], analyComplexRep, time)

if __name__ == "__main__":
    main()
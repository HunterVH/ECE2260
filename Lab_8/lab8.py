import numpy as np
import scipy as sci
import math

def inverseLaplace(const, root, time, inst=1):
    if inst == 1:
        return const*np.exp(root*time)
    else:
        return (const/math.factorial(inst-1))*np.exp(root*time)*time

def identifyRoots(num, den, time):
    answers = np.zeros((len(time)))
    # test = []
    
    r, p, k = sci.signal.residue(num, den)
    print(f'r: {r}\np: {p}\nk: {k}\n')

    for iter in range(len(p)):
        test.append(inverseLaplace(r[iter],p[iter],time))
        answers += test[iter]

    # for iter in range(len(test)):
    #     print(f'{test[iter]}')

    # answers = test[0]+test[1]+test[2]
    
    return answers


    

if __name__ == "__main__":
    time = np.arange(0,1,.01)
    # numerator = np.array([100,300])
    # denominator = np.array([1,12,61,150])

    # identifyRoots(numerator, denominator)

    # numerator = np.array([1,1])
    # denominator = np.array([1,2,1])

    # identifyRoots(numerator, denominator, time)

    numerator = np.array([96,1632,5760])
    denominator = np.array([1,14,48,0])
    test = identifyRoots(numerator,denominator, time)
    for iter in range(len(time)):
        print(f'time: {time[iter]} | value: {test[iter]}')
    